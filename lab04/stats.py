import sys


def parse_record(line: str) -> dict:
    data = line.split(";")
    if len(data) != 3:
        raise ValueError(f"Expect 3 arguments, got {len(data)}")
    city = data[0].strip()
    date = data[2].strip()
    if city == '' or date == '':
        raise ValueError("Date or city is empty")
    try:
        temperature = float(data[1])
    except ValueError:
        raise ValueError(f"Temperature is not a number: {data[1]!r}")
    return {"city": city, "temperature": temperature, "date": date}


def read_valid(lines: list[str]) -> list[dict]:
    res = []
    for line in lines:
        if line.strip() == '':
            continue
        try:
            res.append(parse_record(line))
        except ValueError:
            pass
    return res


def average_by_city(records: list[dict]) -> dict:
    total = {}
    count = {}
    for record in records:
        city = record["city"]
        total[city] = total.get(city, 0.0) + record["temperature"]
        count[city] = count.get(city, 0) + 1

    return {city: round(total[city] / count[city],) for city in total}


def warmest_city(records: list[dict]) -> str:
    averages = average_by_city(records)
    if not averages:
        raise ValueError("Invalid records")

    best = None
    for city in sorted(averages):
        if best is None or averages[city] > averages[best]:
            best = city
    return best
