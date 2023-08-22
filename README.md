# Database Connection Benchmarking

This Python script benchmarks the performance of normal database connections and connection pooling using `pymysql` and `sqlalchemy` libraries.

## Prerequisites

- Python 3.x
- Install required libraries:

    ```
    poetry install
    ```

## Setup

1. **Clone Repo**: Clone this repository.
   
2. **RDS SQL Instance**: Set up an RDS SQL instance or compatible MySQL database. Note down host, user, password, and port.

3. **Configure Database**:
   
   Update `config.py` with your database settings:

   ```python
   db_config = {
       'host': 'your_host',
       'user': 'your_user',
       'password': 'your_password',
       'port': your_port,
   }

## Run Benchmark:

Execute demo.py script:

```
python demo.py
```

## Results:
Script outputs total time queries using normal vs pooled connections. You'll see a difference of how fast the connection pooling option. The difference becomes more significant as the iterations are increased over (default is set to 10). 
