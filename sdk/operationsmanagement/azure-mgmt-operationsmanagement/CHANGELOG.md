# Release History

## 2.0.0b1 (2022-10-27)

### Breaking Changes

  - Operation ManagementAssociationsOperations.create_or_update has a new parameter provider_name
  - Operation ManagementAssociationsOperations.create_or_update has a new parameter resource_name
  - Operation ManagementAssociationsOperations.create_or_update has a new parameter resource_type
  - Operation ManagementAssociationsOperations.delete has a new parameter provider_name
  - Operation ManagementAssociationsOperations.delete has a new parameter resource_name
  - Operation ManagementAssociationsOperations.delete has a new parameter resource_type
  - Operation ManagementAssociationsOperations.get has a new parameter provider_name
  - Operation ManagementAssociationsOperations.get has a new parameter resource_name
  - Operation ManagementAssociationsOperations.get has a new parameter resource_type

## 1.0.0 (2020-12-16)

- GA release

## 1.0.0b1 (2020-11-02)

This is beta preview version.

This version uses a next-generation code generator that introduces important breaking changes, but also important new features (like unified authentication and async programming).

General breaking changes

Credential system has been completly revamped:

azure.common.credentials or msrestazure.azure_active_directory instances are no longer supported, use the azure-identity classes instead: https://pypi.org/project/azure-identity/
credentials parameter has been renamed credential
The config attribute no longer exists on a client, configuration should be passed as kwarg. Example: MyClient(credential, subscription_id, enable_logging=True). For a complete set of supported options, see the parameters accept in init documentation of azure-core

You can't import a version module anymore, use __version__ instead

Operations that used to return a msrest.polling.LROPoller now returns a azure.core.polling.LROPoller and are prefixed with begin_.

Exceptions tree have been simplified and most exceptions are now azure.core.exceptions.HttpResponseError (CloudError has been removed).

Most of the operation kwarg have changed. Some of the most noticeable:

raw has been removed. Equivalent feature can be found using cls, a callback that will give access to internal HTTP response for advanced user
For a complete set of supported options, see the parameters accept in Request documentation of azure-core
General new features

Type annotations support using typing. SDKs are mypy ready.
This client has now stable and official support for async. Check the aio namespace of your package to find the async client.
This client now support natively tracing library like OpenCensus or OpenTelemetry. See this tracing quickstart for an overview.

## 0.1.0 (2020-01-24)

* Initial Release
