import React from "react";
import {
  EuiCode,
  EuiFlexGroup,
  EuiFlexItem,
  EuiPanel,
  EuiSpacer,
  EuiText
} from "@elastic/eui";
import { useOnChangeHandler } from "@gojek/mlp-ui";
import { DraggableHeader } from "../../DraggableHeader";
import { SelectTableOperation } from "./table_operations/SelectTableOperation";
import { ColumnsComboBox } from "./table_operations/ColumnsComboBox";
import { RenameColumns } from "./table_operations/RenameColumns";

export const TableTransformationStepCard = ({
  index = 0,
  step,
  onChangeHandler,
  onDelete,
  errors = {},
  ...props
}) => {
  const { onChange } = useOnChangeHandler(onChangeHandler);

  return (
    <EuiPanel>
      <DraggableHeader
        onDelete={onDelete}
        dragHandleProps={props.dragHandleProps}
      />

      <EuiSpacer size="s" />

      <EuiFlexGroup direction="column" gutterSize="s">
        <EuiFlexItem>
          <EuiText size="s">
            <h4>#{index + 1} Step</h4>
          </EuiText>
        </EuiFlexItem>

        <EuiFlexItem>
          <SelectTableOperation
            operation={step.operation}
            onChangeHandler={onChangeHandler}
            errors={errors}
          />
        </EuiFlexItem>

        <EuiFlexItem>
          {step.operation === "drop" && (
            <ColumnsComboBox
              columns={step.dropColumns || []}
              onChange={onChange("dropColumns")}
              title="Columns to be deleted"
              description={
                <p>
                  This operation will drop one or more columns. Use{" "}
                  <EuiCode>,</EuiCode> as delimiter.
                </p>
              }
            />
          )}

          {step.operation === "rename" && (
            <RenameColumns
              columns={step.renameColumns || {}}
              onChangeHandler={onChangeHandler}
            />
          )}

          {step.operation === "select" && (
            <ColumnsComboBox
              columns={step.selectColumns || []}
              onChange={onChange("selectColumns")}
              title="Columns to be selected"
              description={
                <p>
                  This operation will reorder and drop unselected columns. Use{" "}
                  <EuiCode>,</EuiCode> as delimiter.
                </p>
              }
            />
          )}

          {step.operation === "sort" && <EuiText>sort</EuiText>}

          {step.operation === "update" && <EuiText>update</EuiText>}
        </EuiFlexItem>
      </EuiFlexGroup>
    </EuiPanel>
  );
};
