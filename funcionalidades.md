# Functional Document: How2Burn

This document details all features present in the **How2Burn** app, grouped by their respective functional areas.

---

## 1. Authentication and Access Control
- **Secure Authentication**: Login and account creation managed via Firebase Auth.
- **Approval System (Waitlist)**: New signups go through an approval flow (`Pending`, `Approved`, `Rejected`), ensuring exclusive access or control over the platform.
- **Admin Panel**: Restricted access for administrators to manage user approvals and status directly in the app.

---

## 2. Main Dashboard
The dashboard centralizes daily metrics and the user's metabolic state.
- **Caloric Balance**: Real-time display of calories consumed versus calories burned.
- **Macronutrient Control**: Progress bars for Protein, Carbs, and Fats intake based on daily goals.
- **WHO Limits Monitoring**: Visual alerts for intake of:
  - Sugar
  - Cholesterol
  - Processed Meats
  - Additives and Sweeteners
- **Daily Deficit/Surplus**: Calculation of how much is left to reach the weight loss goal for the day.
- **Automatic Synchronization**: Summary of caloric burn and Basal Metabolic Rate (BMR) synced from Apple Health/Apple Watch.

---

## 3. Logging & Tracking
Data entry tools optimized for zero friction in daily use.
- **Quick Launch**: Global action button (`+`) accessible from any tab.
- **Food Logging**:
  - Meal classification (Breakfast, Snack, Lunch, Dinner, etc.).
  - **AI Recognition (Camera)**: Take a photo of the plate and AI (Gemini Vision) estimates portions and macronutrients.
  - **Voice Recognition**: Dictate what you ate and the AI converts it into nutritional items.
  - **Barcode Scanner**: Scan packaged products (with a nutrient review flow).
  - **Manual Search/Entry**: Search in the database or create food manually.
- **Workout Logging**:
  - Insertion of duration and type of exercise.
  - **AI Calculation**: Uses user biometrics and workout description to estimate exact caloric burn of the session.
- **Weight Logging**: Quick entry of daily weight to calculate progress on the scale.

---

## 4. Journeys (Gamification & Progression)
The "Journeys" tab allows users to track their progress in long or short-term cycles (Sprints).
- **Active Cycle**:
  - Timer showing continuous days, hours, and minutes of the current cycle.
  - Tracking **Theoretical Fat Burn** (based on accumulated deficit) vs. **Real Loss on the Scale**.
  - Visual charts showing weight and caloric deficit evolution over the journey days.
- **Journey History**:
  - Storage of finished cycles.
  - Viewing aggregated reports (e.g., total sugar consumed in 30 days of a journey, average deficit).
- **Grouped Risk Metrics**: Cards evaluating health risk based on ultra-processed foods consumed in the current journey.

---

## 5. Settings & Biometric Profile
Advanced settings for hyper-personalization of the dietary routine.
- **Local Preferences**:
  - Language Selection (System, PT-BR, English, Spanish, French, German, Simplified/Traditional Chinese).
  - Weight measurement units (Kilograms / Pounds).
- **Metabolic Calculation & Goals**:
  - **Basal Metabolic Rate (BMR)**: Integrated automatic calculator using the *Mifflin-St Jeor* equation based on height, weight, sex, and age.
  - **Estimated Exercise (Sedentary to Intense)**: For use when the Apple Watch is not available.
  - **HealthKit Integration**: Toggle to force Apple Watch reading or focus on the app's theoretical calculations.
  - **Fat Loss Goal**: The user sets how many pounds to lose per month, and the app dynamically adjusts the required daily deficit.
  - **Protein Multiplier**: Setting based on intensity (Moderate, Medium, High).
- **Customizable Daily Limits**:
  - Allows users to redefine tolerance margins for Sugar (g), Cholesterol (mg), Processed Meats (g), and Additives (units).
- **Version History**: Tracking of released features and information on the current AI engine (Gemini 3.1 Flash Lite).

---

## 6. Core Technology & Underlying Integrations
- **Backend/Synchronization**: Firebase Firestore for *realtime updates*. Data reflects in real time across all logged devices.
- **Artificial Intelligence**: Native integration with Gemini APIs for log abstraction (Vision, Speech, and Free Text).
- **Health**: Apple HealthKit for reading user's weight, basal expenditure, and active expenditure.
