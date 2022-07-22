# openapi

We uses the `OpenAPI 2.0` to specify our API and to generate SDKs.

## Getting started

Adding finverse.yml will trigger the CICD to build the SDKs.

# Generated SDKs

## GO
Published sdk: https://github.com/finversetech/sdk-go

```
openapi-generator-cli generate \
		--ignore-file-override .openapi-generator-ignore \
		-p packageName=finverse,structPrefix=true,generateInterfaces=true,withCustomMiddlewareFunction=true \
		--global-property=apiTests=false,modelTests=false,apiDocs=false,modelDocs=false \
		-i finverse.yml -g go -o .generated/go/finverse
```

## Typescript
Published sdk: https://github.com/finversetech/sdk-typescript

```
openapi-generator-cli generate --ignore-file-override .openapi-generator-ignore \
        -p packageName=finverse,supportsES6=true,npmName=@finverse/sdk-typescript,withInterfaces=true,npmVersion=0.0.1-$(date +%s) \
        --global-property=apiTests=false,modelTests=false,apiDocs=false,modelDocs=false \
        -i finverse.yml -g typescript-axios -o .generated/ts/finverse

```
