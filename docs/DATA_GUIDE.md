# Dataset guide

The project brief lists restaurant fields (name, links, estimated cost, collection/category, cuisines) and review fields (reviewer, review text, rating, reviewer metadata, time, pictures).

## Preferred format
A merged CSV with one row per restaurant and columns:
- `name` (required; restaurant name)
- `city` (optional)
- `cost` (optional; numeric estimated cost/person)
- `rating` (optional; numeric rating)
- `cuisines` (optional; text, e.g. comma-separated)
- `collection` (optional; category/tag)
- `reviews` (optional; text, ideally concatenated reviews)

Other columns are retained in source data but not used in the core model. If restaurant and review tables are separate, aggregate review text by restaurant identifier/name and merge before running the pipeline. Avoid merging by name alone if duplicate names exist; use a stable restaurant ID where possible.

## Data cleaning checks
- Review column names and types; map source names to expected names.
- Confirm cost and rating units and rating scale.
- Remove duplicate restaurant records carefully.
- Missing numeric values are imputed with median for model features.
- Missing categorical values are filled with `Unknown`.
- Costs/rating should be inspected for invalid values; do not automatically remove valid extremes.

## Demo data
`data/demo_restaurants.csv` is synthetic, intended only to test code and UI. It is not evidence about Zomato or any actual restaurant.
