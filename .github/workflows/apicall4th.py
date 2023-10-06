import requests

url = "https://sagerx-aws-devtest-comm.cloud.databricks.com/api/2.1/jobs/get?job_id=496296034538647"

payload={}
headers = {
  'Authorization': 'Bearer <TOKEN>’
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


Response:
{
    "job_id": 496296034538647,
    "creator_user_name": "shilpa.telmasare@sagerx.com",
    "run_as_user_name": "shilpa.telmasare@sagerx.com",
    "run_as_owner": true,
    "settings": {
        "name": "job_cicd",
        "email_notifications": {
            "no_alert_for_skipped_runs": false
        },
        "webhook_notifications": {},
        "timeout_seconds": 0,
        "max_concurrent_runs": 1,
        "tasks": [
            {
                "task_key": "start",
                "run_if": "ALL_SUCCESS",
                "notebook_task": {
                    "notebook_path": "/Repos/DEV_Repo/comm_med_datahub_dbc/dbc_notebook/common/src/dummy_1",
                    "source": "WORKSPACE"
                },
                "job_cluster_key": "start_cluster",
                "timeout_seconds": 0,
                "email_notifications": {},
                "notification_settings": {
                    "no_alert_for_skipped_runs": false,
                    "no_alert_for_canceled_runs": false,
                    "alert_on_last_attempt": false
                }
            },
            {
                "task_key": "dummy_1",
                "depends_on": [
                    {
                        "task_key": "start"
                    }
                ],
                "run_if": "ALL_SUCCESS",
                "notebook_task": {
                    "notebook_path": "/Repos/DEV_Repo/comm_med_datahub_dbc/dbc_notebook/common/src/dummy_1",
                    "source": "WORKSPACE"
                },
                "job_cluster_key": "start_cluster",
                "timeout_seconds": 0,
                "email_notifications": {},
                "notification_settings": {
                    "no_alert_for_skipped_runs": false,
                    "no_alert_for_canceled_runs": false,
                    "alert_on_last_attempt": false
                }
            },
            {
                "task_key": "dummy_2",
                "depends_on": [
                    {
                        "task_key": "start"
                    }
                ],
                "run_if": "ALL_SUCCESS",
                "notebook_task": {
                    "notebook_path": "/Repos/DEV_Repo/comm_med_datahub_dbc/dbc_notebook/common/src/dummy_2",
                    "source": "WORKSPACE"
                },
                "job_cluster_key": "start_cluster",
                "timeout_seconds": 0,
                "email_notifications": {},
                "notification_settings": {
                    "no_alert_for_skipped_runs": false,
                    "no_alert_for_canceled_runs": false,
                    "alert_on_last_attempt": false
                }
            }
        ],
        "job_clusters": [
            {
                "job_cluster_key": "start_cluster",
                "new_cluster": {
                    "cluster_name": "",
                    "spark_version": "13.2.x-scala2.12",
                    "aws_attributes": {
                        "first_on_demand": 9,
                        "availability": "SPOT_WITH_FALLBACK",
                        "zone_id": "auto",
                        "spot_bid_price_percent": 100,
                        "ebs_volume_count": 0
                    },
                    "node_type_id": "c5d.2xlarge",
                    "driver_node_type_id": "c5d.2xlarge",
                    "custom_tags": {
                        "Function": "Commercial",
                        "Project": "Commercial_DataHub",
                        "Team": "Capgemini",
                        "ClusterOwner": "kathiravan.boopathirajan@sagerx.com"
                    },
                    "spark_env_vars": {
                        "dbc_environment": "DEV"
                    },
                    "enable_elastic_disk": false,
                    "policy_id": "9C61AEBD5500065C",
                    "data_security_mode": "SINGLE_USER",
                    "runtime_engine": "STANDARD",
                    "autoscale": {
                        "min_workers": 1,
                        "max_workers": 8
                    }
                }
            }
        ],
        "format": "MULTI_TASK"
    },
    "created_time": 1692957017770
}
