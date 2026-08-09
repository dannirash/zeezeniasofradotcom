# Zeezenia Farm & Sofra (`zeezeniasofra.com`)

Official web landing page, technical roadmap, and marketing strategy for **Zeezenia Farm & Sofra** — an authentic Egyptian farm-to-table café, U-pick blueberry farm, Bedouin lounge, organic produce market, and halal butcher located in Newberry, FL (30 minutes from UF campus / Gainesville).

---

## 📁 Repository Structure

```
SofraFarm/
├── CNAME                    # Custom domain configuration (zeezeniasofra.com)
├── README.md                # Project documentation & Square marketing strategy
├── .gitignore               # Git ignore rules
├── index.html               # Primary production landing page
├── assets/
│   └── images/
│       ├── raw/             # High-resolution original camera photos (~13MB each)
│       └── web/             # Web-optimized lightweight JPEGs (<100KB each)
├── docs/
│   └── pitch.html           # Internal tech roadmap & publishing pitch document
└── scripts/
    ├── edit_script.py       # HTML text batch modifier script
    └── optimize_images.py   # Automated image compression & format converter script
```

---

## ⚡ Web Performance & Image Optimization

Original camera assets (~51.3 MB raw) are stored safely in `assets/images/raw/`. 

To ensure instant loading times on mobile devices and 3G/4G network connections, run the optimization script to generate web-ready assets in `assets/images/web/`:

```bash
python3 scripts/optimize_images.py
```

- Raw images: `~12.8 MB` each
- Web optimized images: `~75-100 KB` each (**>99% compression ratio** with zero visible quality loss)

---

## 🚀 Deployment Instructions

### Option 1: GitHub Pages (Recommended)
1. Push this repository to GitHub.
2. In GitHub repository settings, navigate to **Pages**.
3. Select `main` branch and root `/` directory.
4. Set custom domain to `zeezeniasofra.com` (handled automatically via `CNAME` file).
5. Enable **Enforce HTTPS**.

### Option 2: Netlify Drop
1. Go to [netlify.com/drop](https://app.netlify.com/drop).
2. Drag and drop the repository folder.
3. In Netlify Domain Management, add `zeezeniasofra.com` as the primary custom domain.

---

## 💳 Square Marketing Strategy & Setup Guide

This codebase is configured to integrate with **Square POS, Square Loyalty, and Square Marketing** for physical and online customer engagement.

### 1. POS Customer Capture (At Checkout)
- Enable **Digital Text/Email Receipts** on all Square POS units at the café and U-Pick register.
- Custom receipt footer message: *"Join the Sofra Club for 10% off your next visit + U-pick blueberry alerts!"*
- Display QR code table tents in the Bedouin Lounge linking customers to the Square digital subscriber form.

### 2. Square Loyalty Program ("Sofra Club")
- **Earn Rate**: 1 Point for every $1 spent at Café, Market, or U-Pick.
- **Reward Tiers**:
  - **50 Points**: Free Fresh Mint Tea or Hibiscus Iced Tea
  - **100 Points**: Free Fresh Mango Lassi or Baklawa Dessert Plate
  - **200 Points**: Free U-Pick Blueberry Bucket or $15 off Weekend Farm Brunch Platter
- **UF Student Special**: Double points on Friday afternoons with valid UF Student ID.

### 3. Automated Square Marketing Campaigns
- **Welcome Email Series**: Triggers instantly on receipt opt-in or web signup. Sends 10% discount code + farm directions.
- **Weekend Café Specials**: Sent every Thursday afternoon featuring Egyptian brunch items and Bedouin lounge specials.
- **Seasonal U-Pick Alerts**: Broadcast blast sent 1 week before blueberry harvest opens.
- **Win-Back Automation**: Sends a 15% incentive to customers who haven't visited in 45 days.

### 4. E-Gift Cards & Pre-Ordering
- Link Square E-Gift Cards on social media (`@zeezeniasofra`) and `index.html`.
- Pre-sell U-Pick time slots and farm event tickets via Square Online.

---

## 🛠 Local Development & Updates

To edit HTML content across production pages:
```bash
python3 scripts/edit_script.py
```

To preview locally, open `index.html` directly in any web browser or use VS Code Live Server.
