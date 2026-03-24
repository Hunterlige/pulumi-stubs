

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
__all__ = ['PipelineJobArgs', 'PipelineJob']
@pulumi.input_type
class PipelineJobArgs:
    def __init__(__self__, *, dataset: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], backfill_pipeline_job: Optional[pulumi.Input[PipelineJobBackfillPipelineJobArgs]] = ..., disable_lineage: Optional[pulumi.Input[_builtins.bool]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., mapping_pipeline_job: Optional[pulumi.Input[PipelineJobMappingPipelineJobArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., reconciliation_pipeline_job: Optional[pulumi.Input[PipelineJobReconciliationPipelineJobArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dataset(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @dataset.setter
    def dataset(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backfillPipelineJob")
    def backfill_pipeline_job(self) -> Optional[pulumi.Input[PipelineJobBackfillPipelineJobArgs]]:
        
        ...
    
    @backfill_pipeline_job.setter
    def backfill_pipeline_job(self, value: Optional[pulumi.Input[PipelineJobBackfillPipelineJobArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableLineage")
    def disable_lineage(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_lineage.setter
    def disable_lineage(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mappingPipelineJob")
    def mapping_pipeline_job(self) -> Optional[pulumi.Input[PipelineJobMappingPipelineJobArgs]]:
        
        ...
    
    @mapping_pipeline_job.setter
    def mapping_pipeline_job(self, value: Optional[pulumi.Input[PipelineJobMappingPipelineJobArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reconciliationPipelineJob")
    def reconciliation_pipeline_job(self) -> Optional[pulumi.Input[PipelineJobReconciliationPipelineJobArgs]]:
        
        ...
    
    @reconciliation_pipeline_job.setter
    def reconciliation_pipeline_job(self, value: Optional[pulumi.Input[PipelineJobReconciliationPipelineJobArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _PipelineJobState:
    def __init__(__self__, *, backfill_pipeline_job: Optional[pulumi.Input[PipelineJobBackfillPipelineJobArgs]] = ..., dataset: Optional[pulumi.Input[_builtins.str]] = ..., disable_lineage: Optional[pulumi.Input[_builtins.bool]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., mapping_pipeline_job: Optional[pulumi.Input[PipelineJobMappingPipelineJobArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., reconciliation_pipeline_job: Optional[pulumi.Input[PipelineJobReconciliationPipelineJobArgs]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backfillPipelineJob")
    def backfill_pipeline_job(self) -> Optional[pulumi.Input[PipelineJobBackfillPipelineJobArgs]]:
        
        ...
    
    @backfill_pipeline_job.setter
    def backfill_pipeline_job(self, value: Optional[pulumi.Input[PipelineJobBackfillPipelineJobArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dataset(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dataset.setter
    def dataset(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableLineage")
    def disable_lineage(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_lineage.setter
    def disable_lineage(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mappingPipelineJob")
    def mapping_pipeline_job(self) -> Optional[pulumi.Input[PipelineJobMappingPipelineJobArgs]]:
        
        ...
    
    @mapping_pipeline_job.setter
    def mapping_pipeline_job(self, value: Optional[pulumi.Input[PipelineJobMappingPipelineJobArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reconciliationPipelineJob")
    def reconciliation_pipeline_job(self) -> Optional[pulumi.Input[PipelineJobReconciliationPipelineJobArgs]]:
        
        ...
    
    @reconciliation_pipeline_job.setter
    def reconciliation_pipeline_job(self, value: Optional[pulumi.Input[PipelineJobReconciliationPipelineJobArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:healthcare/pipelineJob:PipelineJob")
class PipelineJob(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., backfill_pipeline_job: Optional[pulumi.Input[Union[PipelineJobBackfillPipelineJobArgs, PipelineJobBackfillPipelineJobArgsDict]]] = ..., dataset: Optional[pulumi.Input[_builtins.str]] = ..., disable_lineage: Optional[pulumi.Input[_builtins.bool]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., mapping_pipeline_job: Optional[pulumi.Input[Union[PipelineJobMappingPipelineJobArgs, PipelineJobMappingPipelineJobArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., reconciliation_pipeline_job: Optional[pulumi.Input[Union[PipelineJobReconciliationPipelineJobArgs, PipelineJobReconciliationPipelineJobArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: PipelineJobArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., backfill_pipeline_job: Optional[pulumi.Input[Union[PipelineJobBackfillPipelineJobArgs, PipelineJobBackfillPipelineJobArgsDict]]] = ..., dataset: Optional[pulumi.Input[_builtins.str]] = ..., disable_lineage: Optional[pulumi.Input[_builtins.bool]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., mapping_pipeline_job: Optional[pulumi.Input[Union[PipelineJobMappingPipelineJobArgs, PipelineJobMappingPipelineJobArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., reconciliation_pipeline_job: Optional[pulumi.Input[Union[PipelineJobReconciliationPipelineJobArgs, PipelineJobReconciliationPipelineJobArgsDict]]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ...) -> PipelineJob:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backfillPipelineJob")
    def backfill_pipeline_job(self) -> pulumi.Output[Optional[outputs.PipelineJobBackfillPipelineJob]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dataset(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableLineage")
    def disable_lineage(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mappingPipelineJob")
    def mapping_pipeline_job(self) -> pulumi.Output[Optional[outputs.PipelineJobMappingPipelineJob]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reconciliationPipelineJob")
    def reconciliation_pipeline_job(self) -> pulumi.Output[Optional[outputs.PipelineJobReconciliationPipelineJob]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


