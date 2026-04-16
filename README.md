# E-commerce Conversion Funnel Analysis

This project analyzes user behavior in a large multi-category e-commerce platform to understand conversion patterns (view → cart → purchase).

## Objective
- Analyze user journey through the funnel
- Identify drop-off points
- Interpret behavioral patterns affecting conversion
- Provide data-driven recommendations to improve conversion performance and address business problems

## Dataset
- Source: Kaggle  
  https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store
- Provider: REES46 Marketing Platform  
  https://rees46.com/
- Description:
  The dataset contains user interaction events (view, cart, remove_from_cart, purchase) from a large e-commerce platform.  
  Each row represents an event linking users and products within sessions.

## Key Features
- event_time — timestamp of event (UTC)
- event_type — user action (view, cart, remove_from_cart, purchase)
- product_id — product identifier
- category_id — product category ID
- category_code — category taxonomy
- brand — product brand (nullable)
- price — product price
- user_id — user identifier
- user_session — session identifier

## Project Structure
- data/
  - raw/        → original dataset files
  - interim/    → intermediate processed data
  - processed/  → final analysis-ready data
- src/
  - etl/        → extract, transform, load pipeline
- notebooks/
  - analysis notebooks

## Notes
- Dataset contains multiple months of data (Oct 2019 – Apr 2020)
- Each session may contain multiple events including multiple purchases