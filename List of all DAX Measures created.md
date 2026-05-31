# DAX Measures

## Top DAX Functions Used

* CALCULATE()
* AVERAGE()
* COUNT() / COUNTROWS()
* FILTER()
* DIVIDE()
* RANKX()
* DISTINCTCOUNT()
* ALL()
* ALLEXCEPT()
* VAR / RETURN

---

## 1. Accuracy

```DAX
Accuracy =
AVERAGE(Listings[review_scores_accuracy])
```

## 2. Avg Nightly Price

```DAX
Avg Nightly Price =
AVERAGE(Listings[price])
```

## 3. Avg Price

```DAX
Avg Price =
AVERAGE(Listings[price])
```

## 4. Avg Rating

```DAX
Avg Rating =
AVERAGE(Listings[review_scores_rating])
```

## 5. City Rank

```DAX
City Rank =
RANKX(
    ALL(Listings[city]),
    [Total Listing],
    ,
    DESC
)
```

## 6. Cleanliness

```DAX
Cleanliness =
AVERAGE(Listings[review_scores_cleanliness])
```

## 7. Communication

```DAX
Communication =
AVERAGE(Listings[review_scores_communication])
```

## 8. Cumulative %

```DAX
Cumulative % =
DIVIDE(
    [Cumulative Listings],
    CALCULATE(
        [Total Listing],
        ALL(Listings[city])
    )
)
```

## 9. Cumulative Listings

```DAX
Cumulative Listings =
VAR CurrentRank =
    MAXX(
        VALUES(Listings[city]),
        [City Rank]
    )
RETURN
    CALCULATE(
        [Total Listing],
        FILTER(
            ALL(Listings[city]),
            [City Rank] <= CurrentRank
        )
    )
```

## 10. Entire Place

```DAX
Entire Place =
CALCULATE(
    COUNT(Listings[listing_id]),
    Listings[room_type] = "Entire place"
)
```

## 11. Hotel Room

```DAX
Hotel Room =
CALCULATE(
    COUNT(Listings[listing_id]),
    Listings[room_type] = "Hotel room"
)
```

## 12. Location

```DAX
Location =
AVERAGE(Listings[review_scores_location])
```

## 13. Net Sentiment Score

```DAX
Net Sentiment Score =
CALCULATE(
    COUNTROWS(listings_with_sentiment),
    listings_with_sentiment[sentiment] = "Positive"
)
-
CALCULATE(
    COUNTROWS(listings_with_sentiment),
    listings_with_sentiment[sentiment] = "Negative"
)
```

## 14. No Superhost Listings

```DAX
No Superhost Listings =
CALCULATE(
    COUNT(Listings[listing_id]),
    Listings[host_is_superhost] = "f"
)
```

## 15. Private Room

```DAX
Private Room =
CALCULATE(
    COUNT(Listings[listing_id]),
    Listings[room_type] = "Private room"
)
```

## 16. Shared Room

```DAX
Shared Room =
CALCULATE(
    COUNT(Listings[listing_id]),
    Listings[room_type] = "Shared room"
)
```

## 17. Superhost Listings

```DAX
Superhost Listings =
CALCULATE(
    COUNT(Listings[listing_id]),
    Listings[host_is_superhost] = "t"
)
```

## 18. Total Listing

```DAX
Total Listing =
COUNT(Listings[listing_id])
```

## 19. Value

```DAX
Value =
AVERAGE(Listings[review_scores_value])
```

## 20. Cumulative % Review Frequency

```DAX
Cumulative % Review Frequency =
DIVIDE(
    [Cumulative Reviewers],
    [Reviewers]
)
```

## 21. Cumulative Reviewers

```DAX
Cumulative Reviewers =
VAR CurrentReviews =
    MAX(Reviews[Reviews per Reviewer])
RETURN
    CALCULATE(
        DISTINCTCOUNT(Reviews[reviewer_id]),
        FILTER(
            ALL(Reviews[Reviews per Reviewer]),
            Reviews[Reviews per Reviewer] <= CurrentReviews
        )
    )
```

## 22. Reviewers

```DAX
Reviewers =
DISTINCTCOUNT(Reviews[reviewer_id])
```

## 23. Reviews per Reviewer

```DAX
Reviews per Reviewer =
CALCULATE(
    COUNT(Reviews[review_id]),
    ALLEXCEPT(
        Reviews,
        Reviews[reviewer_id]
    )
)
```
