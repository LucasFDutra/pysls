# SUMMARY
- [alexa-skills-kit](#alexa-skills-kit)
- [alexa-smart-home](#alexa-smart-home)
- [apigateway](#apigateway)
- [batch](#batch)
- [cloudformation](#cloudformation)
- [cloudfront](#cloudfront)
- [codecommit](#codecommit)
- [codepipeline](#codepipeline)
- [cognito](#cognito)
- [config](#config)
- [connect](#connect)
- [dynamodb](#dynamodb)
- [cloudwatch](#cloudwatch)
- [kinesis](#kinesis)
- [lex](#lex)
- [rekognition](#rekognition)
- [s3](#s3)
- [sagemaker](#sagemaker)
- [ses](#ses)
- [sns](#sns)
- [sqs](#sqs)
- [stepfunctions](#stepfunctions)
---


## alexa-skills-kit
| Event | Params |
| - | - |
| end-session | `--session-id`  `--user-id`  `--application-id`  `--request-id`   |
| intent-answer | `--session-id`  `--user-id`  `--application-id`  `--request-id`   |
| intent-getnewfact | `--session-id`  `--user-id`  `--application-id`  `--request-id`   |
| intent-mycoloris | `--session-id`  `--user-id`  `--application-id`  `--request-id`   |
| intent-recipe | `--session-id`  `--user-id`  `--application-id`  `--request-id`   |
| start-session | `--session-id`  `--user-id`  `--application-id`  `--request-id`   |
---


## alexa-smart-home
| Event | Params |
| - | - |
| smart-home-control-turn-off-request |  |
| smart-home-control-turn-on-request |  |
| smart-home-discovery-request |  |
---


## apigateway
| Event | Params |
| - | - |
| authorizer | `--account-id`  `--partition`  `--region`  `--stage`  `--method`  `--resource`  `--restApiId`   |
| aws-proxy | `--body`  `--stage`  `--method`  `--resource`  `--path`  `--account-id`  `--dns-suffix`   |
---


## batch
| Event | Params |
| - | - |
| get-job |  |
| submit-job |  |
---


## cloudformation
| Event | Params |
| - | - |
| create-request | `--account-id`  `--partition`  `--region`  `--stack`   |
---


## cloudfront
| Event | Params |
| - | - |
| ab-test | `--uri`  `--method`   |
| access-request-in-response | `--uri`  `--method`   |
| http-redirect | `--uri`  `--method`   |
| modify-querystring | `--uri`  `--method`   |
| modify-response-header |  |
| multiple-remote-calls-aggregate-response | `--uri`  `--method`   |
| normalize-querystring-to-improve-cache-hit | `--uri`  `--method`   |
| redirect-on-viewer-country | `--uri`  `--method`   |
| redirect-unauthenticated-users | `--uri`  `--method`   |
| response-generation | `--uri`  `--method`   |
| serve-object-on-viewer-device | `--uri`  `--method`   |
| simple-remote-call | `--uri`  `--method`   |
---


## codecommit
| Event | Params |
| - | - |
| repository | `--account-id`  `--partition`  `--region`  `--repository`  `--trigger`  `--custom-data`   |
---


## codepipeline
| Event | Params |
| - | - |
| job | `--account-id`  `--input-bucket`  `--input-key`  `--output-bucket`  `--output-key`   |
---


## cognito
| Event | Params |
| - | - |
| sync-trigger | `--region`   |
---


## config
| Event | Params |
| - | - |
| item-change-notification | `--region`  `--partition`  `--account-id`   |
| oversized-item-change-notification | `--region`  `--partition`  `--account-id`   |
| periodic-rule | `--region`  `--partition`  `--account-id`   |
---


## connect
| Event | Params |
| - | - |
| contact-flow-event | `--region`  `--partition`  `--account-id`  `--contact-id`  `--phone-number`   |
---


## dynamodb
| Event | Params |
| - | - |
| update | `--account-id`  `--partition`  `--region`  `--table`   |
---


## cloudwatch
| Event | Params |
| - | - |
| logs |  |
| scheduled-event | `--account-id`  `--partition`  `--region`  `--rule`   |
---


## kinesis
| Event | Params |
| - | - |
| get-records | `--region`  `--partition`  `--sequence`  `--data`  `--partition-key`   |
| kinesis-firehose | `--partition`  `--region`  `--data`   |
| analytics | `--partition`  `--region`  `--account-id`  `--application`  `--stream`  `--data`   |
| analytics-compressed | `--partition`  `--region`  `--account-id`  `--application`  `--stream`  `--data`   |
| analytics-dynamodb | `--partition`  `--region`  `--account-id`  `--application`  `--stream`  `--data`   |
| analytics-kpl | `--partition`  `--region`  `--account-id`  `--application`  `--stream`   |
| apachelog | `--region`  `--data`   |
| cloudwatch-logs-processor | `--region`  `--partition`  `--account-id`   |
| streams-as-source | `--partition`  `--region`  `--partition-key`  `--data`  `--sequence`   |
| syslog | `--region`  `--data`   |
---


## lex
| Event | Params |
| - | - |
| book-car |  |
| book-hotel |  |
| make-appointment |  |
| order-flowers |  |
---


## rekognition
| Event | Params |
| - | - |
| s3-request | `--region`  `--partition`  `--bucket`  `--key`   |
---


## s3
| Event | Params |
| - | - |
| delete | `--region`  `--partition`  `--bucket`  `--key`   |
| put | `--region`  `--partition`  `--bucket`  `--key`   |
---


## sagemaker
| Event | Params |
| - | - |
| ground-truth-pre-human | `--region`  `--partition`  `--account-id`  `--source-ref`  `--labeling-job-name`   |
| ground-truth-annotation-consolidation | `--region`  `--partition`  `--account-id`  `--labeling-job-name`  `--label-attribute-name`  `--s3-output-path`  `--execution-role`  `--iteration-object-timestamp`   |
---


## ses
| Event | Params |
| - | - |
| email-receiving | `--region`  `--partition`  `--account-id`  `--dns-suffix`   |
---


## sns
| Event | Params |
| - | - |
| notification | `--account-id`  `--partition`  `--region`  `--topic`  `--subject`  `--message`   |
---


## sqs
| Event | Params |
| - | - |
| receive-message | `--partition`  `--region`  `--account-id`  `--queue-name`  `--body`   |
---


## stepfunctions
| Event | Params |
| - | - |
| error |  |
---


