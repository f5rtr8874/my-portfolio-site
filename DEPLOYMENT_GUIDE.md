# Portfolio Website - Simple Deployment Guide

This guide will help you deploy your portfolio website using **Vercel** (frontend) and **Railway** (backend).

## 🚀 Quick Deployment Steps

### Step 1: Deploy Backend to Railway

1. **Sign up for Railway**
   - Go to [railway.app](https://railway.app)
   - Sign up with your GitHub account

2. **Deploy Backend**
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your GitHub repository
   - Railway will automatically detect the Python app
   - Set these environment variables in Railway:
     ```
     PORT=8001
     MONGO_URL=mongodb://localhost:27017/portfolio_db
     ```

3. **Get Your Backend URL**
   - After deployment, Railway will give you a URL like:
   - `https://your-app-name.railway.app`
   - **Copy this URL** - you'll need it for the frontend!

### Step 2: Deploy Frontend to Vercel

1. **Sign up for Vercel**
   - Go to [vercel.com](https://vercel.com)
   - Sign up with your GitHub account

2. **Deploy Frontend**
   - Click "New Project" → Select your GitHub repository
   - Vercel will automatically detect the React app
   - Set these environment variables in Vercel:
     ```
     VITE_BACKEND_URL=https://your-backend-url.railway.app
     ```
   - Replace `your-backend-url.railway.app` with your actual Railway URL

3. **Configure Build Settings**
   - Root Directory: `frontend`
   - Build Command: `yarn build`
   - Output Directory: `dist`

### Step 3: Update Database (Optional)

For production, you might want to use a cloud database:

1. **MongoDB Atlas (Free)**
   - Go to [mongodb.com/cloud/atlas](https://mongodb.com/cloud/atlas)
   - Create a free cluster
   - Get your connection string
   - Update `MONGO_URL` in Railway to your Atlas connection string

## 🔧 Files Already Prepared

I've created these deployment files for you:

- `vercel.json` - Vercel configuration
- `railway.json` - Railway configuration  
- `Procfile` - Alternative Railway startup
- Updated `requirements.txt` - Python dependencies
- Updated `package.json` - Build scripts

## 📱 Environment Variables Summary

### Railway (Backend)
```
PORT=8001
MONGO_URL=mongodb://localhost:27017/portfolio_db
```

### Vercel (Frontend)
```
VITE_BACKEND_URL=https://your-backend-url.railway.app
```

## 🎉 That's It!

After following these steps:
1. Your backend will be live on Railway
2. Your frontend will be live on Vercel
3. Both will be connected and working together

## 🆘 Need Help?

If you run into issues:
1. Check the deployment logs in Railway/Vercel dashboards
2. Verify your environment variables are set correctly
3. Make sure your Backend URL is properly configured in frontend

Your portfolio website is now ready for deployment! 🚀