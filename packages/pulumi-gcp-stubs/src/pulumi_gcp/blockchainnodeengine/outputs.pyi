import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "BlockchainNodesConnectionInfo",
    "BlockchainNodesConnectionInfoEndpointInfo",
    "BlockchainNodesEthereumDetails",
    "BlockchainNodesEthereumDetailsAdditionalEndpoint",
    "BlockchainNodesEthereumDetailsGethDetails",
    "BlockchainNodesEthereumDetailsValidatorConfig",
]

@pulumi.output_type
class BlockchainNodesConnectionInfo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        endpoint_infos: Optional[
            Sequence[outputs.BlockchainNodesConnectionInfoEndpointInfo]
        ] = ...,
        service_attachment: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointInfos")
    def endpoint_infos(
        self,
    ) -> Optional[Sequence[outputs.BlockchainNodesConnectionInfoEndpointInfo]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAttachment")
    def service_attachment(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BlockchainNodesConnectionInfoEndpointInfo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        json_rpc_api_endpoint: Optional[_builtins.str] = ...,
        websockets_api_endpoint: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jsonRpcApiEndpoint")
    def json_rpc_api_endpoint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="websocketsApiEndpoint")
    def websockets_api_endpoint(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BlockchainNodesEthereumDetails(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        additional_endpoints: Optional[
            Sequence[outputs.BlockchainNodesEthereumDetailsAdditionalEndpoint]
        ] = ...,
        api_enable_admin: Optional[_builtins.bool] = ...,
        api_enable_debug: Optional[_builtins.bool] = ...,
        consensus_client: Optional[_builtins.str] = ...,
        execution_client: Optional[_builtins.str] = ...,
        geth_details: Optional[outputs.BlockchainNodesEthereumDetailsGethDetails] = ...,
        network: Optional[_builtins.str] = ...,
        node_type: Optional[_builtins.str] = ...,
        validator_config: Optional[
            outputs.BlockchainNodesEthereumDetailsValidatorConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalEndpoints")
    def additional_endpoints(
        self,
    ) -> Optional[
        Sequence[outputs.BlockchainNodesEthereumDetailsAdditionalEndpoint]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="apiEnableAdmin")
    def api_enable_admin(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="apiEnableDebug")
    def api_enable_debug(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="consensusClient")
    def consensus_client(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="executionClient")
    def execution_client(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gethDetails")
    def geth_details(
        self,
    ) -> Optional[outputs.BlockchainNodesEthereumDetailsGethDetails]: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="validatorConfig")
    def validator_config(
        self,
    ) -> Optional[outputs.BlockchainNodesEthereumDetailsValidatorConfig]: ...

@pulumi.output_type
class BlockchainNodesEthereumDetailsAdditionalEndpoint(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        beacon_api_endpoint: Optional[_builtins.str] = ...,
        beacon_prometheus_metrics_api_endpoint: Optional[_builtins.str] = ...,
        execution_client_prometheus_metrics_api_endpoint: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="beaconApiEndpoint")
    def beacon_api_endpoint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="beaconPrometheusMetricsApiEndpoint")
    def beacon_prometheus_metrics_api_endpoint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="executionClientPrometheusMetricsApiEndpoint")
    def execution_client_prometheus_metrics_api_endpoint(
        self,
    ) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BlockchainNodesEthereumDetailsGethDetails(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, garbage_collection_mode: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="garbageCollectionMode")
    def garbage_collection_mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BlockchainNodesEthereumDetailsValidatorConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, mev_relay_urls: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mevRelayUrls")
    def mev_relay_urls(self) -> Optional[Sequence[_builtins.str]]: ...
