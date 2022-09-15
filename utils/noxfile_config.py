import tempfile


# Airflow creates a config file at the installation, so we want to set
# `AIRFLOW_HOME` envvar before running pytest.

_tmpdir = tempfile.TemporaryDirectory()

TEST_CONFIG_OVERRIDE = {
    # You can opt out from the test for specific Python versions.
    "ignored_versions": [
        "2.7",
        "3.6",
        "3.7",
        "3.9",
        "3.10",
    ],  # Composer w/ Airflow 2 only supports Python 3.8
    # Old samples are opted out of enforcing Python type hints
    # All new samples should feature them
    "enforce_type_hints": True,
    # An envvar key for determining the project id to use. Change it
    # to 'BUILD_SPECIFIC_GCLOUD_PROJECT' if you want to opt in using a
    # build specific Cloud project. You can also use your own string
    # to use your own Cloud project.
    "gcloud_project_env": "GOOGLE_CLOUD_PROJECT",
    # 'gcloud_project_env': 'BUILD_SPECIFIC_GCLOUD_PROJECT',
    # If you need to use a specific version of pip,
    # change pip_version_override to the string representation
    # of the version number, for example, "20.2.4"
    "pip_version_override": "20.2.4",
    # A dictionary you want to inject into your test. Don't put any
    # secrets here. These values will override predefined values.
    "envs": {"AIRFLOW_HOME": _tmpdir.name},
}
