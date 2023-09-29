import pathway as pw


def concat_with_titles(**kwargs) -> str:
    combined = [f"{title}: {value}" for title, value in kwargs.items()]
    return ', '.join(combined)


def transform(sales_data):
    return sales_data.select(
        doc=pw.apply(concat_with_titles, **sales_data),
    )
