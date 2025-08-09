import os
import time

import psycopg2

from app.core import clean_sum


def wait_for_db():
    for _ in range(30):
        try:
            with psycopg2.connect(
                host=os.getenv("DB_HOST", "db"),
                port=os.getenv("DB_PORT", "5432"),
                user=os.getenv("DB_USER", "postgres"),
                password=os.getenv("DB_PASS", "postgres"),
                dbname=os.getenv("DB_NAME", "postgres"),
            ):
                return
        except Exception:
            time.sleep(1)
    raise SystemExit("DB not ready after retries")


def main():
    wait_for_db()
    with psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        port=os.getenv("DB_PORT", "5432"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASS", "postgres"),
        dbname=os.getenv("DB_NAME", "postgres"),
    ) as conn:
        with conn.cursor() as cur:
            cur.execute("CREATE TABLE IF NOT EXISTS nums(x int PRIMARY KEY)")
            for v in (1, 2, 3):
                cur.execute("INSERT INTO nums(x) VALUES (%s) ON CONFLICT DO NOTHING", (v,))
            conn.commit()
            cur.execute("SELECT SUM(x) FROM nums")
            (s,) = cur.fetchone()
            print(f"✅ sum_in_db={s}")


if __name__ == "__main__":
    print("✅ sum =", clean_sum([1, None, 2, 3]))
    main()
