import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "BlockchainNodesConnectionInfoArgs",
    "BlockchainNodesConnectionInfoArgsDict",
    "BlockchainNodesConnectionInfoEndpointInfoArgs",
    "BlockchainNodesConnectionInfoEndpointInfoArgsDict",
    "BlockchainNodesEthereumDetailsArgs",
    "BlockchainNodesEthereumDetailsArgsDict",
    ...,
    ...,
    "BlockchainNodesEthereumDetailsGethDetailsArgs",
    "BlockchainNodesEthereumDetailsGethDetailsArgsDict",
    "BlockchainNodesEthereumDetailsValidatorConfigArgs",
    ...,
]

class BlockchainNodesConnectionInfoArgsDict(TypedDict):
    endpoint_infos: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[BlockchainNodesConnectionInfoEndpointInfoArgsDict]]
        ]
    ]
    service_attachment: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class BlockchainNodesConnectionInfoArgs:
    def __init__(
        __self__,
        *,
        endpoint_infos: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[BlockchainNodesConnectionInfoEndpointInfoArgs]]
            ]
        ] = ...,
        service_attachment: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointInfos")
    def endpoint_infos(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[BlockchainNodesConnectionInfoEndpointInfoArgs]]
        ]
    ]: ...
    @endpoint_infos.setter
    def endpoint_infos(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[BlockchainNodesConnectionInfoEndpointInfoArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAttachment")
    def service_attachment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_attachment.setter
    def service_attachment(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BlockchainNodesConnectionInfoEndpointInfoArgsDict(TypedDict):
    json_rpc_api_endpoint: NotRequired[pulumi.Input[_builtins.str]]
    websockets_api_endpoint: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class BlockchainNodesConnectionInfoEndpointInfoArgs:
    def __init__(
        __self__,
        *,
        json_rpc_api_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        websockets_api_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jsonRpcApiEndpoint")
    def json_rpc_api_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @json_rpc_api_endpoint.setter
    def json_rpc_api_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="websocketsApiEndpoint")
    def websockets_api_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @websockets_api_endpoint.setter
    def websockets_api_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BlockchainNodesEthereumDetailsArgsDict(TypedDict):
    additional_endpoints: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[BlockchainNodesEthereumDetailsAdditionalEndpointArgsDict]
            ]
        ]
    ]
    api_enable_admin: NotRequired[pulumi.Input[_builtins.bool]]
    api_enable_debug: NotRequired[pulumi.Input[_builtins.bool]]
    consensus_client: NotRequired[pulumi.Input[_builtins.str]]
    execution_client: NotRequired[pulumi.Input[_builtins.str]]
    geth_details: NotRequired[
        pulumi.Input[BlockchainNodesEthereumDetailsGethDetailsArgsDict]
    ]
    network: NotRequired[pulumi.Input[_builtins.str]]
    node_type: NotRequired[pulumi.Input[_builtins.str]]
    validator_config: NotRequired[
        pulumi.Input[BlockchainNodesEthereumDetailsValidatorConfigArgsDict]
    ]
    ...

@pulumi.input_type
class BlockchainNodesEthereumDetailsArgs:
    def __init__(
        __self__,
        *,
        additional_endpoints: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[BlockchainNodesEthereumDetailsAdditionalEndpointArgs]
                ]
            ]
        ] = ...,
        api_enable_admin: Optional[pulumi.Input[_builtins.bool]] = ...,
        api_enable_debug: Optional[pulumi.Input[_builtins.bool]] = ...,
        consensus_client: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_client: Optional[pulumi.Input[_builtins.str]] = ...,
        geth_details: Optional[
            pulumi.Input[BlockchainNodesEthereumDetailsGethDetailsArgs]
        ] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        node_type: Optional[pulumi.Input[_builtins.str]] = ...,
        validator_config: Optional[
            pulumi.Input[BlockchainNodesEthereumDetailsValidatorConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalEndpoints")
    def additional_endpoints(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[BlockchainNodesEthereumDetailsAdditionalEndpointArgs]]
        ]
    ]: ...
    @additional_endpoints.setter
    def additional_endpoints(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[BlockchainNodesEthereumDetailsAdditionalEndpointArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="apiEnableAdmin")
    def api_enable_admin(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @api_enable_admin.setter
    def api_enable_admin(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="apiEnableDebug")
    def api_enable_debug(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @api_enable_debug.setter
    def api_enable_debug(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="consensusClient")
    def consensus_client(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @consensus_client.setter
    def consensus_client(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="executionClient")
    def execution_client(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @execution_client.setter
    def execution_client(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gethDetails")
    def geth_details(
        self,
    ) -> Optional[pulumi.Input[BlockchainNodesEthereumDetailsGethDetailsArgs]]: ...
    @geth_details.setter
    def geth_details(
        self,
        value: Optional[pulumi.Input[BlockchainNodesEthereumDetailsGethDetailsArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_type.setter
    def node_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="validatorConfig")
    def validator_config(
        self,
    ) -> Optional[pulumi.Input[BlockchainNodesEthereumDetailsValidatorConfigArgs]]: ...
    @validator_config.setter
    def validator_config(
        self,
        value: Optional[
            pulumi.Input[BlockchainNodesEthereumDetailsValidatorConfigArgs]
        ],
    ): ...

class BlockchainNodesEthereumDetailsAdditionalEndpointArgsDict(TypedDict):
    beacon_api_endpoint: NotRequired[pulumi.Input[_builtins.str]]
    beacon_prometheus_metrics_api_endpoint: NotRequired[pulumi.Input[_builtins.str]]
    execution_client_prometheus_metrics_api_endpoint: NotRequired[
        pulumi.Input[_builtins.str]
    ]
    ...

@pulumi.input_type
class BlockchainNodesEthereumDetailsAdditionalEndpointArgs:
    def __init__(
        __self__,
        *,
        beacon_api_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        beacon_prometheus_metrics_api_endpoint: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        execution_client_prometheus_metrics_api_endpoint: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="beaconApiEndpoint")
    def beacon_api_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @beacon_api_endpoint.setter
    def beacon_api_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="beaconPrometheusMetricsApiEndpoint")
    def beacon_prometheus_metrics_api_endpoint(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @beacon_prometheus_metrics_api_endpoint.setter
    def beacon_prometheus_metrics_api_endpoint(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="executionClientPrometheusMetricsApiEndpoint")
    def execution_client_prometheus_metrics_api_endpoint(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @execution_client_prometheus_metrics_api_endpoint.setter
    def execution_client_prometheus_metrics_api_endpoint(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class BlockchainNodesEthereumDetailsGethDetailsArgsDict(TypedDict):
    garbage_collection_mode: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class BlockchainNodesEthereumDetailsGethDetailsArgs:
    def __init__(
        __self__,
        *,
        garbage_collection_mode: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="garbageCollectionMode")
    def garbage_collection_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @garbage_collection_mode.setter
    def garbage_collection_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BlockchainNodesEthereumDetailsValidatorConfigArgsDict(TypedDict):
    mev_relay_urls: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class BlockchainNodesEthereumDetailsValidatorConfigArgs:
    def __init__(
        __self__,
        *,
        mev_relay_urls: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mevRelayUrls")
    def mev_relay_urls(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @mev_relay_urls.setter
    def mev_relay_urls(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
