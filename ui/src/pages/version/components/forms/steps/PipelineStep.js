import React, { useContext } from "react";
import { EuiFlexGroup, EuiFlexItem } from "@elastic/eui";
import {
  FormContext,
  FormValidationContext,
  get,
  useOnChangeHandler
} from "@gojek/mlp-ui";
import { GraphPanel } from "../components/transformer/components/GraphPanel";
import { InputPanel } from "../components/transformer/InputPanel";
import { OutputPanel } from "../components/transformer/OutputPanel";
import { TransformationPanel } from "../components/transformer/TransformationPanel";
import { FeastProjectsContextProvider } from "../../../../../providers/feast/FeastProjectsContext";

export const PipelineStep = ({ stage }) => {
  const {
    data: {
      transformer: {
        config: {
          [stage]: { inputs, transformations, outputs }
        }
      }
    },
    onChangeHandler
  } = useContext(FormContext);
  const { onChange } = useOnChangeHandler(onChangeHandler);
  const { errors } = useContext(FormValidationContext);

  return (
    <EuiFlexGroup className="KELAS">
      <EuiFlexItem grow={7}>
        <EuiFlexGroup direction="column" gutterSize="m">
          <EuiFlexItem grow={false}>
            <FeastProjectsContextProvider>
              <InputPanel
                inputs={inputs}
                onChangeHandler={onChange(`transformer.config.${stage}.inputs`)}
                errors={get(errors, `transformer.config.${stage}.inputs`)}
              />
            </FeastProjectsContextProvider>
          </EuiFlexItem>

          <EuiFlexItem grow={false}>
            <TransformationPanel
              transformations={transformations}
              onChangeHandler={onChange(
                `transformer.config.${stage}.transformations`
              )}
              errors={get(
                errors,
                `transformer.config.${stage}.transformations`
              )}
            />
          </EuiFlexItem>

          <EuiFlexItem grow={false}>
            <OutputPanel
              outputs={outputs}
              onChangeHandler={onChange(`transformer.config.${stage}.outputs`)}
              errors={get(errors, `transformer.config.${stage}.outputs`)}
            />
          </EuiFlexItem>
        </EuiFlexGroup>
      </EuiFlexItem>

      <EuiFlexItem grow={3}>
        <GraphPanel />
      </EuiFlexItem>
    </EuiFlexGroup>
  );
};
