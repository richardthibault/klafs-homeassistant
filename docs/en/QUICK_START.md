# Quick Start Guide

**Read in other languages:** **English** | [Français](../fr/QUICK_START.md) | [Deutsch](../de/QUICK_START.md) | [Español](../es/QUICK_START.md)

## 🚀 Installation in 3 Steps

### Step 1: Install via HACS (Recommended)

1. Open **HACS** in Home Assistant
2. Go to **Integrations**
3. Click the **three dots** in the top right
4. Select **Custom repositories**
5. Add URL: `https://github.com/richardthibault/klafs-homeassistant`
6. Category: **Integration**
7. Search for **"Klafs Sauna"**
8. Click **Download**

### Step 2: Restart Home Assistant

- Via UI: **Settings** > **System** > **Restart**
- Via CLI: `ha core restart`

### Step 3: Configure Integration

1. Go to **Settings** > **Devices & Services**
2. Click **+ Add Integration**
3. Search for **"Klafs Sauna"**
4. Follow the 3 steps:
   - **Step 1**: Enter your Klafs Sauna App credentials
   - **Step 2**: Select your saunas
   - **Step 3**: Enter PIN codes (optional)

## ✅ Verification

### 1. Check integration is loaded
- Go to **Settings** > **Devices & Services**
- "Klafs Sauna" should appear in the list

### 2. Check logs
- **Settings** > **System** > **Logs**
- Search for "klafs" to see integration messages

### 3. Check created entities
- Go to **Settings** > **Devices & Services** > **Entities**
- Filter by "klafs"
- You should see entities for your sauna(s)

## 🐛 Common Issues

### Integration doesn't appear in HACS

**Solution:**
1. Verify you added the custom repository
2. Refresh HACS (Menu > Reload data)
3. Restart Home Assistant

### "Invalid credentials" error

**Solution:**
1. Verify your credentials at https://sauna-app.klafs.com
2. Warning: 3 failed attempts = account blocked
3. Wait 30 minutes or contact Klafs

### No sauna detected

**Solution:**
1. Verify your sauna is configured in the Klafs app
2. Check the Wi-Fi module is connected
3. Test from the Klafs mobile app

## 📚 Complete Documentation

- [README.md](../../README.md) - Main documentation
- [INSTALLATION.md](INSTALLATION.md) - Detailed installation guide
- [TESTING.md](TESTING.md) - Complete testing guide
- [TROUBLESHOOTING.md](TROUBLESHOOTING.md) - Troubleshooting

## 💡 Help

- **GitHub Issues**: [Create an issue](https://github.com/richardthibault/klafs-homeassistant/issues)
- **HA Forum**: https://community.home-assistant.io
- **HA Discord**: #custom-components channel

## 🎉 That's it!

Your Klafs integration is now installed and ready to use!
