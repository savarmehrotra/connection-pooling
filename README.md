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


#Notes 

## What is Connection Pooling?

Connection pooling is a technique used to efficiently manage and reuse database connections in applications, reducing the overhead of creating and closing connections for every database operation.

## What is a Session?

A session represents a workspace for interacting with the database. It allows you to perform CRUD (Create, Read, Update, Delete) operations on database objects.

## What is a Session Factory?

A Session Factory, often created using the `Sessionmaker` function, is used to create session objects. It takes the database engine as an argument and produces session instances.

## Parameters that can be tuned:

- `pool_size`: Defines the number of connections to keep open.
- `max_overflow`: Sets the maximum number of connections that can be created beyond the pool size when needed.

## Benefits of Connection Pooling:

- Improved performance: Reusing existing connections reduces connection overhead.
- Efficient resource utilization: Limits the number of simultaneous database connections.
- Automatic connection management: SQLAlchemy handles connection creation and disposal.

Connections can be recycled after a certain period of inactivity or closed when they are no longer needed. Connections will be recycled every hour (`pool_recycle`) and will timeout after 30 seconds of idle time (`pool_timeout`).

## Disadvantages:

- Connection Leaks
- Unused resources
- Stale Connections

## Pool Size (`pool_size`):

**Rule of Thumb:** Match the pool size to your expected application concurrency, typically between 5 to 20 connections.

## Max Overflow (`max_overflow`):

**Rule of Thumb:** Use a conservative value (1 to 5) to limit extra connections beyond the pool size.

## Pool Recycle (`pool_recycle`):

**Rule of Thumb:** Set a reasonable interval (e.g., 1 hour) for refreshing connections based on database behavior.

