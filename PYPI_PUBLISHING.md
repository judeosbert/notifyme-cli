# PyPI Publishing Guide

## 🚀 **Publishing notifyme-cli to PyPI**

This guide covers both manual publishing and automated GitHub Actions publishing.

## 📋 **Prerequisites**

### 1. **Create PyPI Accounts**

You'll need accounts on both:
- **PyPI (Production)**: https://pypi.org/account/register/
- **Test PyPI (Testing)**: https://test.pypi.org/account/register/

### 2. **Generate API Tokens**

After creating accounts, generate API tokens:

**For PyPI:**
1. Go to https://pypi.org/manage/account/token/
2. Click "Add API token"
3. Token name: `notifyme-cli-publishing`
4. Scope: "Entire account" (or create project first and scope to project)
5. **Save the token securely** - you won't see it again!

**For Test PyPI:**
1. Go to https://test.pypi.org/manage/account/token/
2. Follow same steps as above

## 🛠️ **Method 1: Manual Publishing**

### Step 1: Install Publishing Tools

```bash
pip install build twine
# Or using the dev dependencies
pip install -e ".[dev]"
```

### Step 2: Configure Credentials

Create `~/.pypirc` file:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-YOUR_ACTUAL_PYPI_TOKEN_HERE

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-YOUR_ACTUAL_TESTPYPI_TOKEN_HERE
```

**⚠️ Important:** Replace `YOUR_ACTUAL_*_TOKEN_HERE` with your actual tokens!

### Step 3: Build and Test

```bash
# Clean previous builds
make clean

# Build the package
make build

# Check the distribution
make check-dist
```

### Step 4: Test on Test PyPI

```bash
# Upload to Test PyPI first
make upload-test

# Test installation from Test PyPI
pip install --index-url https://test.pypi.org/simple/ notifyme-cli
```

### Step 5: Publish to PyPI

```bash
# If test worked, upload to real PyPI
make upload
```

## 🤖 **Method 2: Automated GitHub Publishing**

This is already set up in `.github/workflows/publish.yml`!

### Step 1: Add GitHub Secrets

In your GitHub repository:

1. Go to **Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret**
3. Add these secrets:

**Required Secrets:**
- Name: `PYPI_API_TOKEN`
- Value: Your PyPI API token (starts with `pypi-`)

**Optional (for test publishing):**
- Name: `TEST_PYPI_API_TOKEN` 
- Value: Your Test PyPI API token

### Step 2: Create a Release

The workflow triggers on GitHub releases:

```bash
# Tag the release
git tag v1.0.0
git push origin v1.0.0

# Or create release through GitHub UI:
# 1. Go to your repo → Releases → Create new release
# 2. Tag: v1.0.0
# 3. Title: v1.0.0 - Initial Release
# 4. Description: Copy from CHANGELOG.md
# 5. Publish release
```

### Step 3: Monitor Workflow

- GitHub Actions will automatically build and publish to PyPI
- Check the **Actions** tab for progress
- If successful, your package will be live on PyPI!

## 🎯 **Publishing Checklist**

Before publishing, ensure:

- [ ] **Version updated** in `setup.py` and `__init__.py`
- [ ] **CHANGELOG.md updated** with release notes
- [ ] **All tests pass** (`make test`)
- [ ] **Code formatted** (`make format` and `make lint`)
- [ ] **Documentation updated** (README.md, etc.)
- [ ] **Git committed and pushed**

## 🔍 **Verification After Publishing**

```bash
# Install from PyPI
pip install notifyme-cli

# Test the installation
notifyme --version
notifyme --help

# Test functionality (if configured)
notifyme test
```

## 🚨 **Troubleshooting**

### Common Issues:

**"Package already exists"**
- You can't overwrite existing versions
- Increment version number in `setup.py`

**"Invalid credentials"**
- Check your API token is correct
- Ensure token has proper permissions
- Token might have expired

**"Build fails"**
- Run `make test` and `make lint` locally first
- Check all files are committed to git

**"Import errors after install"**
- Check `setup.py` entry points are correct
- Verify package structure matches `find_packages()`

## 🎉 **Success!**

After successful publishing:

1. **Share the good news!** 📢
   ```bash
   pip install notifyme-cli
   ```

2. **Update documentation** with PyPI install instructions

3. **Monitor downloads** at https://pypi.org/project/notifyme-cli/

4. **Handle issues** via GitHub Issues

## 🔄 **Future Updates**

For future releases:
1. Update version number
2. Update CHANGELOG.md
3. Create new GitHub release
4. Automatic publishing via GitHub Actions! 

---

**Need help?** The maintainer setup has been automated - just create a GitHub release and the rest happens automatically! 🤖