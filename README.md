# Airflow as Scheduler

A docker-compose file demostrates how to use Airflow scheduler as a cron-like service.

It's overkill to use Airflow scheduler as a simple cron service. It presents some desirable features, though.

- Highly available: Jobs still would be picked up if a scheduler instance failed.
- Load balanced: The jobs(dags) are scheduled and balanced among all active schedulers.

## Prerequsites

This tutorial assumes docker and docker-compose are already installed.

## Get Started

Initialize database:

```sh
docker-compose up airflow-init
```

Start the services:

```sh
docker-compose up
```

There are two schedulers are set up in this tutorial so that you may play around by shutting one of thme down. For example, to shutdown the scheduler a, you may use following command;

```sh
docker-compose stop airflow-scheduler-a
```

## Web UI

You may access the web UI after the services are launched successfully.
Open the url `http://localhost:8080`, and log in with default username and password (airflow:airflow).
