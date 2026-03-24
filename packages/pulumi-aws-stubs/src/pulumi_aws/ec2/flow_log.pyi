

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['FlowLogArgs', 'FlowLog']
@pulumi.input_type
class FlowLogArgs:
    def __init__(__self__, *, deliver_cross_account_role: Optional[pulumi.Input[_builtins.str]] = ..., destination_options: Optional[pulumi.Input[FlowLogDestinationOptionsArgs]] = ..., eni_id: Optional[pulumi.Input[_builtins.str]] = ..., iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., log_destination: Optional[pulumi.Input[_builtins.str]] = ..., log_destination_type: Optional[pulumi.Input[_builtins.str]] = ..., log_format: Optional[pulumi.Input[_builtins.str]] = ..., max_aggregation_interval: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., regional_nat_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., traffic_type: Optional[pulumi.Input[_builtins.str]] = ..., transit_gateway_attachment_id: Optional[pulumi.Input[_builtins.str]] = ..., transit_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deliverCrossAccountRole")
    def deliver_cross_account_role(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deliver_cross_account_role.setter
    def deliver_cross_account_role(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationOptions")
    def destination_options(self) -> Optional[pulumi.Input[FlowLogDestinationOptionsArgs]]:
        
        ...
    
    @destination_options.setter
    def destination_options(self, value: Optional[pulumi.Input[FlowLogDestinationOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eniId")
    def eni_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @eni_id.setter
    def eni_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @iam_role_arn.setter
    def iam_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logDestination")
    def log_destination(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_destination.setter
    def log_destination(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logDestinationType")
    def log_destination_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_destination_type.setter
    def log_destination_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logFormat")
    def log_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_format.setter
    def log_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAggregationInterval")
    def max_aggregation_interval(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_aggregation_interval.setter
    def max_aggregation_interval(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionalNatGatewayId")
    def regional_nat_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @regional_nat_gateway_id.setter
    def regional_nat_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trafficType")
    def traffic_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @traffic_type.setter
    def traffic_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayAttachmentId")
    def transit_gateway_attachment_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @transit_gateway_attachment_id.setter
    def transit_gateway_attachment_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @transit_gateway_id.setter
    def transit_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _FlowLogState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., deliver_cross_account_role: Optional[pulumi.Input[_builtins.str]] = ..., destination_options: Optional[pulumi.Input[FlowLogDestinationOptionsArgs]] = ..., eni_id: Optional[pulumi.Input[_builtins.str]] = ..., iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., log_destination: Optional[pulumi.Input[_builtins.str]] = ..., log_destination_type: Optional[pulumi.Input[_builtins.str]] = ..., log_format: Optional[pulumi.Input[_builtins.str]] = ..., max_aggregation_interval: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., regional_nat_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., traffic_type: Optional[pulumi.Input[_builtins.str]] = ..., transit_gateway_attachment_id: Optional[pulumi.Input[_builtins.str]] = ..., transit_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deliverCrossAccountRole")
    def deliver_cross_account_role(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deliver_cross_account_role.setter
    def deliver_cross_account_role(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationOptions")
    def destination_options(self) -> Optional[pulumi.Input[FlowLogDestinationOptionsArgs]]:
        
        ...
    
    @destination_options.setter
    def destination_options(self, value: Optional[pulumi.Input[FlowLogDestinationOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eniId")
    def eni_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @eni_id.setter
    def eni_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @iam_role_arn.setter
    def iam_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logDestination")
    def log_destination(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_destination.setter
    def log_destination(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logDestinationType")
    def log_destination_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_destination_type.setter
    def log_destination_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logFormat")
    def log_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_format.setter
    def log_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAggregationInterval")
    def max_aggregation_interval(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_aggregation_interval.setter
    def max_aggregation_interval(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionalNatGatewayId")
    def regional_nat_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @regional_nat_gateway_id.setter
    def regional_nat_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trafficType")
    def traffic_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @traffic_type.setter
    def traffic_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayAttachmentId")
    def transit_gateway_attachment_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @transit_gateway_attachment_id.setter
    def transit_gateway_attachment_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @transit_gateway_id.setter
    def transit_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:ec2/flowLog:FlowLog")
class FlowLog(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., deliver_cross_account_role: Optional[pulumi.Input[_builtins.str]] = ..., destination_options: Optional[pulumi.Input[Union[FlowLogDestinationOptionsArgs, FlowLogDestinationOptionsArgsDict]]] = ..., eni_id: Optional[pulumi.Input[_builtins.str]] = ..., iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., log_destination: Optional[pulumi.Input[_builtins.str]] = ..., log_destination_type: Optional[pulumi.Input[_builtins.str]] = ..., log_format: Optional[pulumi.Input[_builtins.str]] = ..., max_aggregation_interval: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., regional_nat_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., traffic_type: Optional[pulumi.Input[_builtins.str]] = ..., transit_gateway_attachment_id: Optional[pulumi.Input[_builtins.str]] = ..., transit_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[FlowLogArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., deliver_cross_account_role: Optional[pulumi.Input[_builtins.str]] = ..., destination_options: Optional[pulumi.Input[Union[FlowLogDestinationOptionsArgs, FlowLogDestinationOptionsArgsDict]]] = ..., eni_id: Optional[pulumi.Input[_builtins.str]] = ..., iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., log_destination: Optional[pulumi.Input[_builtins.str]] = ..., log_destination_type: Optional[pulumi.Input[_builtins.str]] = ..., log_format: Optional[pulumi.Input[_builtins.str]] = ..., max_aggregation_interval: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., regional_nat_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., traffic_type: Optional[pulumi.Input[_builtins.str]] = ..., transit_gateway_attachment_id: Optional[pulumi.Input[_builtins.str]] = ..., transit_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ...) -> FlowLog:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deliverCrossAccountRole")
    def deliver_cross_account_role(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationOptions")
    def destination_options(self) -> pulumi.Output[Optional[outputs.FlowLogDestinationOptions]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eniId")
    def eni_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logDestination")
    def log_destination(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logDestinationType")
    def log_destination_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logFormat")
    def log_format(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAggregationInterval")
    def max_aggregation_interval(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionalNatGatewayId")
    def regional_nat_gateway_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trafficType")
    def traffic_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayAttachmentId")
    def transit_gateway_attachment_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


