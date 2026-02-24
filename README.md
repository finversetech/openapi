# openapi

We uses the `OpenAPI 2.0` to specify our API and to generate SDKs.
See `finverse.yml`.

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

## Troubleshooting

If we make backward incompatible changes to API then we may run into errors like the following in the pipeline to publish Typescript SDK.
```
Run `npm audit` for details.
> @finverse/sdk-typescript@0.0.1 build
> tsc --outDir dist
test/responses/transaction.ts(23,9): error TS2322: Type '{ account_id: string; amount: { currency: string; raw: string; value: number; }; created_at: string; description: string; is_pending: false; posted_date: string; transaction_id: string; transfer_details: null; updated_at: string; }' is not assignable to type 'Transaction'.
  Object literal may only specify known properties, and 'transfer_details' does not exist in type 'Transaction'.
test/responses/transaction.ts(38,9): error TS2322: Type '{ account_id: string; amount: { currency: string; raw: string; value: number; }; created_at: string; description: string; is_pending: false; posted_date: string; transaction_id: string; transfer_details: null; updated_at: string; }' is not assignable to type 'Transaction'.
```

The reason for this failure is we may have references to the `modified / removed` fields inside `/test/` and running a build will fail. In order to fix it we will have to manually checkout https://github.com/finversetech/sdk-typescript and then either remove / update the field and push. This may require admin to give permission to this repository.
