# Decap CMS Setup Guide

This guide helps you set up the Decap CMS interface for managing your AJOK website content.

## Quick Start (For Non-Technical Users)

1. **Access the CMS**: Go to `https://your-website.com/admin/` 
2. **Log in**: Use your GitHub account
3. **Edit content**: Click on any collection to edit
4. **Save**: Click "Publish" to save changes live

## Setup Instructions (For Admin/Developers)

### Step 1: Update Backend Configuration

Edit `/admin/config.yml` and change these lines:

```yaml
backend:
  repo: USERNAME/ajok-website  # Replace with your GitHub username
  site_domain: your-domain.com  # Replace with your actual domain
```

### Step 2: Choose Your Hosting Method

#### Option A: Netlify (Recommended - Free)
1. Connect your GitHub repo to Netlify (https://app.netlify.com)
2. Netlify will automatically handle GitHub OAuth authentication
3. Your CMS will be at `https://your-netlify-domain.netlify.app/admin`
4. Board members can login with their GitHub account

**Setup Steps:**
- Push code to GitHub
- Go to Netlify.com and sign up
- Click "New site from Git"
- Select your GitHub repo
- Deploy! 🎉

#### Option B: GitHub OAuth (Manual)
1. Go to GitHub Profile > Settings > Developer settings > OAuth Apps
2. Click "New OAuth App"
3. Fill in:
   - Application name: `AJOK CMS`
   - Homepage URL: `https://your-domain.com`
   - Authorization callback URL: `https://api.netlify.com/auth/done` (if using Netlify)
4. Copy the Client ID and Client Secret
5. If using Netlify, add these as environment variables

### Step 3: Add Board Members

1. Go to your GitHub repo settings
2. Add board members as **Collaborators**
3. They can now login to `/admin` with their GitHub account

### Step 4: Testing

1. Go to `http://localhost:4000/admin` (for local development)
2. Or go to `https://your-domain.com/admin` (live)
3. Try logging in with a GitHub account that has access to the repo
4. Make a small edit and click "Publish"

## Editable Content

The CMS allows you to edit:

### Pages
- Home page sections
- About page
- Camps page
- Volunteers page
- Contact page
- Support page

### Data Collections
- **Navigation**: Menu items
- **Camps**: Camp details, dates, prices
- **Locations**: Camp location information
- **Contact**: Email, phone, social media
- **Forms**: Registration form links
- **Volunteer Functions**: Role descriptions
- **RVB Members**: Board member info
- **Sponsors**: Sponsorship information
- **Testimonials**: Volunteer testimonials
- **Peters/Meters**: Special roles
- **WhatsApp Groups**: Group links

## File Structure

```
admin/
├── index.html        # CMS interface
└── config.yml        # CMS configuration (YOU NEED TO EDIT THIS!)

_data/
├── home/            # Home page content
├── about/           # About page content
├── camps/           # Camps page content
├── volunteers/      # Volunteers page content
├── contact/         # Contact page content
└── support/         # Support page content
```

## Troubleshooting

### "Authentication Failed"
- Make sure your GitHub OAuth credentials are correct
- If using Netlify, check that environment variables are set
- Make sure you're accessing `/admin` (with trailing slash)

### "No collections appearing"
- Make sure all data files exist in `_data/`
- Check that `config.yml` has correct file paths
- Refresh the page (Ctrl+Shift+R for cache clear)

### "Changes not showing on website"
- Make sure you clicked "Publish" (not just "Save")
- Check that GitHub Actions workflow runs successfully
- The site rebuilds automatically after each publish

## Advanced Usage

### Creating New Content Collections

To add a new collection to the CMS:

1. Create a new YAML file in `_data/`
2. Add a new collection config in `/admin/config.yml`
3. Use the pattern from existing collections

Example:
```yaml
- name: my_collection
  label: My Collection
  folder: _data
  files:
    - name: my_data
      label: My Data
      file: _data/my_data.yml
      fields:
        - { label: "Title", name: "title", widget: "string" }
```

### Using Content in Templates

Reference data in your Jekyll templates:

```liquid
{{ site.data.home.intro.title }}
{{ site.data.camps.intro.text }}
```

## Support

For more info on Decap CMS:
- Official Docs: https://decapcms.org/docs/
- GitHub Issues: https://github.com/decaporg/decap-cms
