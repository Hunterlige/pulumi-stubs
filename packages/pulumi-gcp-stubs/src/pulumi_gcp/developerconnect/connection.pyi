import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ConnectionArgs", "Connection"]

@pulumi.input_type
class ConnectionArgs:
    def __init__(
        __self__,
        *,
        connection_id: pulumi.Input[_builtins.str],
        location: pulumi.Input[_builtins.str],
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        bitbucket_cloud_config: Optional[
            pulumi.Input[ConnectionBitbucketCloudConfigArgs]
        ] = ...,
        bitbucket_data_center_config: Optional[
            pulumi.Input[ConnectionBitbucketDataCenterConfigArgs]
        ] = ...,
        crypto_key_config: Optional[pulumi.Input[ConnectionCryptoKeyConfigArgs]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        github_config: Optional[pulumi.Input[ConnectionGithubConfigArgs]] = ...,
        github_enterprise_config: Optional[
            pulumi.Input[ConnectionGithubEnterpriseConfigArgs]
        ] = ...,
        gitlab_config: Optional[pulumi.Input[ConnectionGitlabConfigArgs]] = ...,
        gitlab_enterprise_config: Optional[
            pulumi.Input[ConnectionGitlabEnterpriseConfigArgs]
        ] = ...,
        http_config: Optional[pulumi.Input[ConnectionHttpConfigArgs]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionId")
    def connection_id(self) -> pulumi.Input[_builtins.str]: ...
    @connection_id.setter
    def connection_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def annotations(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @annotations.setter
    def annotations(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="bitbucketCloudConfig")
    def bitbucket_cloud_config(
        self,
    ) -> Optional[pulumi.Input[ConnectionBitbucketCloudConfigArgs]]: ...
    @bitbucket_cloud_config.setter
    def bitbucket_cloud_config(
        self, value: Optional[pulumi.Input[ConnectionBitbucketCloudConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="bitbucketDataCenterConfig")
    def bitbucket_data_center_config(
        self,
    ) -> Optional[pulumi.Input[ConnectionBitbucketDataCenterConfigArgs]]: ...
    @bitbucket_data_center_config.setter
    def bitbucket_data_center_config(
        self, value: Optional[pulumi.Input[ConnectionBitbucketDataCenterConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cryptoKeyConfig")
    def crypto_key_config(
        self,
    ) -> Optional[pulumi.Input[ConnectionCryptoKeyConfigArgs]]: ...
    @crypto_key_config.setter
    def crypto_key_config(
        self, value: Optional[pulumi.Input[ConnectionCryptoKeyConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="githubConfig")
    def github_config(self) -> Optional[pulumi.Input[ConnectionGithubConfigArgs]]: ...
    @github_config.setter
    def github_config(
        self, value: Optional[pulumi.Input[ConnectionGithubConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="githubEnterpriseConfig")
    def github_enterprise_config(
        self,
    ) -> Optional[pulumi.Input[ConnectionGithubEnterpriseConfigArgs]]: ...
    @github_enterprise_config.setter
    def github_enterprise_config(
        self, value: Optional[pulumi.Input[ConnectionGithubEnterpriseConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="gitlabConfig")
    def gitlab_config(self) -> Optional[pulumi.Input[ConnectionGitlabConfigArgs]]: ...
    @gitlab_config.setter
    def gitlab_config(
        self, value: Optional[pulumi.Input[ConnectionGitlabConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="gitlabEnterpriseConfig")
    def gitlab_enterprise_config(
        self,
    ) -> Optional[pulumi.Input[ConnectionGitlabEnterpriseConfigArgs]]: ...
    @gitlab_enterprise_config.setter
    def gitlab_enterprise_config(
        self, value: Optional[pulumi.Input[ConnectionGitlabEnterpriseConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpConfig")
    def http_config(self) -> Optional[pulumi.Input[ConnectionHttpConfigArgs]]: ...
    @http_config.setter
    def http_config(self, value: Optional[pulumi.Input[ConnectionHttpConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _ConnectionState:
    def __init__(
        __self__,
        *,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        bitbucket_cloud_config: Optional[
            pulumi.Input[ConnectionBitbucketCloudConfigArgs]
        ] = ...,
        bitbucket_data_center_config: Optional[
            pulumi.Input[ConnectionBitbucketDataCenterConfigArgs]
        ] = ...,
        connection_id: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        crypto_key_config: Optional[pulumi.Input[ConnectionCryptoKeyConfigArgs]] = ...,
        delete_time: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        effective_annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        github_config: Optional[pulumi.Input[ConnectionGithubConfigArgs]] = ...,
        github_enterprise_config: Optional[
            pulumi.Input[ConnectionGithubEnterpriseConfigArgs]
        ] = ...,
        gitlab_config: Optional[pulumi.Input[ConnectionGitlabConfigArgs]] = ...,
        gitlab_enterprise_config: Optional[
            pulumi.Input[ConnectionGitlabEnterpriseConfigArgs]
        ] = ...,
        http_config: Optional[pulumi.Input[ConnectionHttpConfigArgs]] = ...,
        installation_states: Optional[
            pulumi.Input[Sequence[pulumi.Input[ConnectionInstallationStateArgs]]]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        reconciling: Optional[pulumi.Input[_builtins.bool]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def annotations(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @annotations.setter
    def annotations(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="bitbucketCloudConfig")
    def bitbucket_cloud_config(
        self,
    ) -> Optional[pulumi.Input[ConnectionBitbucketCloudConfigArgs]]: ...
    @bitbucket_cloud_config.setter
    def bitbucket_cloud_config(
        self, value: Optional[pulumi.Input[ConnectionBitbucketCloudConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="bitbucketDataCenterConfig")
    def bitbucket_data_center_config(
        self,
    ) -> Optional[pulumi.Input[ConnectionBitbucketDataCenterConfigArgs]]: ...
    @bitbucket_data_center_config.setter
    def bitbucket_data_center_config(
        self, value: Optional[pulumi.Input[ConnectionBitbucketDataCenterConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="connectionId")
    def connection_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connection_id.setter
    def connection_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cryptoKeyConfig")
    def crypto_key_config(
        self,
    ) -> Optional[pulumi.Input[ConnectionCryptoKeyConfigArgs]]: ...
    @crypto_key_config.setter
    def crypto_key_config(
        self, value: Optional[pulumi.Input[ConnectionCryptoKeyConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete_time.setter
    def delete_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_annotations.setter
    def effective_annotations(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_labels.setter
    def effective_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="githubConfig")
    def github_config(self) -> Optional[pulumi.Input[ConnectionGithubConfigArgs]]: ...
    @github_config.setter
    def github_config(
        self, value: Optional[pulumi.Input[ConnectionGithubConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="githubEnterpriseConfig")
    def github_enterprise_config(
        self,
    ) -> Optional[pulumi.Input[ConnectionGithubEnterpriseConfigArgs]]: ...
    @github_enterprise_config.setter
    def github_enterprise_config(
        self, value: Optional[pulumi.Input[ConnectionGithubEnterpriseConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="gitlabConfig")
    def gitlab_config(self) -> Optional[pulumi.Input[ConnectionGitlabConfigArgs]]: ...
    @gitlab_config.setter
    def gitlab_config(
        self, value: Optional[pulumi.Input[ConnectionGitlabConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="gitlabEnterpriseConfig")
    def gitlab_enterprise_config(
        self,
    ) -> Optional[pulumi.Input[ConnectionGitlabEnterpriseConfigArgs]]: ...
    @gitlab_enterprise_config.setter
    def gitlab_enterprise_config(
        self, value: Optional[pulumi.Input[ConnectionGitlabEnterpriseConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpConfig")
    def http_config(self) -> Optional[pulumi.Input[ConnectionHttpConfigArgs]]: ...
    @http_config.setter
    def http_config(self, value: Optional[pulumi.Input[ConnectionHttpConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="installationStates")
    def installation_states(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ConnectionInstallationStateArgs]]]
    ]: ...
    @installation_states.setter
    def installation_states(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ConnectionInstallationStateArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @pulumi_labels.setter
    def pulumi_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @reconciling.setter
    def reconciling(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:developerconnect/connection:Connection")
class Connection(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        bitbucket_cloud_config: Optional[
            pulumi.Input[
                Union[
                    ConnectionBitbucketCloudConfigArgs,
                    ConnectionBitbucketCloudConfigArgsDict,
                ]
            ]
        ] = ...,
        bitbucket_data_center_config: Optional[
            pulumi.Input[
                Union[
                    ConnectionBitbucketDataCenterConfigArgs,
                    ConnectionBitbucketDataCenterConfigArgsDict,
                ]
            ]
        ] = ...,
        connection_id: Optional[pulumi.Input[_builtins.str]] = ...,
        crypto_key_config: Optional[
            pulumi.Input[
                Union[ConnectionCryptoKeyConfigArgs, ConnectionCryptoKeyConfigArgsDict]
            ]
        ] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        github_config: Optional[
            pulumi.Input[
                Union[ConnectionGithubConfigArgs, ConnectionGithubConfigArgsDict]
            ]
        ] = ...,
        github_enterprise_config: Optional[
            pulumi.Input[
                Union[
                    ConnectionGithubEnterpriseConfigArgs,
                    ConnectionGithubEnterpriseConfigArgsDict,
                ]
            ]
        ] = ...,
        gitlab_config: Optional[
            pulumi.Input[
                Union[ConnectionGitlabConfigArgs, ConnectionGitlabConfigArgsDict]
            ]
        ] = ...,
        gitlab_enterprise_config: Optional[
            pulumi.Input[
                Union[
                    ConnectionGitlabEnterpriseConfigArgs,
                    ConnectionGitlabEnterpriseConfigArgsDict,
                ]
            ]
        ] = ...,
        http_config: Optional[
            pulumi.Input[Union[ConnectionHttpConfigArgs, ConnectionHttpConfigArgsDict]]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ConnectionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        bitbucket_cloud_config: Optional[
            pulumi.Input[
                Union[
                    ConnectionBitbucketCloudConfigArgs,
                    ConnectionBitbucketCloudConfigArgsDict,
                ]
            ]
        ] = ...,
        bitbucket_data_center_config: Optional[
            pulumi.Input[
                Union[
                    ConnectionBitbucketDataCenterConfigArgs,
                    ConnectionBitbucketDataCenterConfigArgsDict,
                ]
            ]
        ] = ...,
        connection_id: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        crypto_key_config: Optional[
            pulumi.Input[
                Union[ConnectionCryptoKeyConfigArgs, ConnectionCryptoKeyConfigArgsDict]
            ]
        ] = ...,
        delete_time: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        effective_annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        github_config: Optional[
            pulumi.Input[
                Union[ConnectionGithubConfigArgs, ConnectionGithubConfigArgsDict]
            ]
        ] = ...,
        github_enterprise_config: Optional[
            pulumi.Input[
                Union[
                    ConnectionGithubEnterpriseConfigArgs,
                    ConnectionGithubEnterpriseConfigArgsDict,
                ]
            ]
        ] = ...,
        gitlab_config: Optional[
            pulumi.Input[
                Union[ConnectionGitlabConfigArgs, ConnectionGitlabConfigArgsDict]
            ]
        ] = ...,
        gitlab_enterprise_config: Optional[
            pulumi.Input[
                Union[
                    ConnectionGitlabEnterpriseConfigArgs,
                    ConnectionGitlabEnterpriseConfigArgsDict,
                ]
            ]
        ] = ...,
        http_config: Optional[
            pulumi.Input[Union[ConnectionHttpConfigArgs, ConnectionHttpConfigArgsDict]]
        ] = ...,
        installation_states: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ConnectionInstallationStateArgs,
                            ConnectionInstallationStateArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        reconciling: Optional[pulumi.Input[_builtins.bool]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Connection: ...
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="bitbucketCloudConfig")
    def bitbucket_cloud_config(
        self,
    ) -> pulumi.Output[Optional[outputs.ConnectionBitbucketCloudConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="bitbucketDataCenterConfig")
    def bitbucket_data_center_config(
        self,
    ) -> pulumi.Output[Optional[outputs.ConnectionBitbucketDataCenterConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="connectionId")
    def connection_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cryptoKeyConfig")
    def crypto_key_config(
        self,
    ) -> pulumi.Output[Optional[outputs.ConnectionCryptoKeyConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="githubConfig")
    def github_config(
        self,
    ) -> pulumi.Output[Optional[outputs.ConnectionGithubConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="githubEnterpriseConfig")
    def github_enterprise_config(
        self,
    ) -> pulumi.Output[Optional[outputs.ConnectionGithubEnterpriseConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="gitlabConfig")
    def gitlab_config(
        self,
    ) -> pulumi.Output[Optional[outputs.ConnectionGitlabConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="gitlabEnterpriseConfig")
    def gitlab_enterprise_config(
        self,
    ) -> pulumi.Output[Optional[outputs.ConnectionGitlabEnterpriseConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="httpConfig")
    def http_config(self) -> pulumi.Output[Optional[outputs.ConnectionHttpConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="installationStates")
    def installation_states(
        self,
    ) -> pulumi.Output[Sequence[outputs.ConnectionInstallationState]]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
