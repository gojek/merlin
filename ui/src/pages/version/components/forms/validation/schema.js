import * as yup from "yup";
import { appConfig } from "../../../../../config";

const cpuRequestRegex = /^(\d{1,3}(\.\d{1,3})?)$|^(\d{2,5}m)$/,
  memRequestRegex = /^\d+(Ei?|Pi?|Ti?|Gi?|Mi?|Ki?)?$/,
  envVariableNameRegex = /^[a-z0-9_]*$/i,
  dockerImageRegex = /^([a-z0-9]+(?:[._-][a-z0-9]+)*(?::\d{2,5})?\/)?([a-z0-9]+(?:[._-][a-z0-9]+)*\/)*([a-z0-9]+(?:[._-][a-z0-9]+)*)(?::[a-z0-9]+(?:[._-][a-z0-9]+)*)?$/i;

const resourceRequestSchema = yup.object().shape({
  cpu_request: yup
    .string()
    .matches(cpuRequestRegex, 'Valid CPU value is required, e.g "2" or "500m"'),
  memory_request: yup
    .string()
    .matches(memRequestRegex, "Valid RAM value is required, e.g. 512Mi"),
  min_replica: yup
    .number()
    .typeError("Min Replicas value is required")
    .min(0, "Min Replicas cannot be less than 0"),
  max_replica: yup
    .number()
    .typeError("Max Replicas value is required")
    .min(
      yup.ref(`min_replica`),
      "Max Replicas cannot be less than Min Replicas"
    )
    .max(
      appConfig.scaling.maxAllowedReplica,
      // eslint-disable-next-line no-template-curly-in-string
      "Max Replicas value has exceeded allowed number of replicas: ${max}"
    )
    .when("min_replica", (minReplica, schema) =>
      minReplica === 0
        ? schema.positive("Max Replica should be positive")
        : schema
    )
});

const environmentVariableSchema = yup.object().shape({
  name: yup
    .string()
    .required("Variable name is required")
    .matches(
      envVariableNameRegex,
      "The name of a variable can contain only alphanumeric character or the underscore"
    ),
  value: yup.string()
});

export const versionEndpointSchema = yup.object().shape({
  environment_name: yup.string().required("Environment is required"),
  resource_request: resourceRequestSchema,
  env_vars: yup.array(environmentVariableSchema)
});

export const transformerConfigSchema = yup.object().shape({
  transformer: yup.object().shape({
    resource_request: resourceRequestSchema,
    env_vars: yup.array(environmentVariableSchema)
  })
});

const dockerImageSchema = yup
  .string()
  .matches(
    dockerImageRegex,
    "Valid Docker Image value should be provided, e.g. kennethreitz/httpbin:latest"
  );

export const customTransformerSchema = yup.object().shape({
  transformer: yup.object().shape({
    image: dockerImageSchema.required("Docker Image is required"),
    command: yup.string(),
    args: yup.string()
  })
});

const feastEntitiesSchema = yup.object().shape({
  name: yup.string().required("Entity Name is required"),
  valueType: yup.string().required("Entity Value Type is required"),
  fieldType: yup.string().required("Input Type is required"),
  field: yup.string().required("Input Value is required")
});

const feastFeaturesSchema = yup.object().shape({
  name: yup.string().required("Feature Name is required")
});

const feastInputConfigSchema = yup.object().shape({
  tableName: yup.string().when("isTableNameEditable", {
    is: true,
    then: yup.string().required("Table name is required")
  }),
  project: yup.string().required("Project name is required"),
  entities: yup.array(feastEntitiesSchema),
  features: yup.array(feastFeaturesSchema)
});

const inputPipelineSchema = yup.object().shape({
  feast: yup.array(feastInputConfigSchema)
});

const transformationPipelineSchema = yup.object().shape({
  inputs: yup.array(inputPipelineSchema)
  // transformations: yup.array(),
  // outputs: yup.array(),
});

export const standardTransformerSchema = yup.object().shape({
  transformer: yup.object().shape({
    config: yup.object().shape({
      feast: yup.array(feastInputConfigSchema),
      preprocess: transformationPipelineSchema
    })
  })
});
