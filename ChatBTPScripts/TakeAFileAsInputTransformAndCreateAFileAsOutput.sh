# Standard Pattern which could be used for any transformation for a large amount of file and afterwards leveraging diff for the review
# -a > uses plain ascii as output into the temporary file transformed_application.yaml
#  mv transformed_application.yaml ui-application.yaml copies the output to the original file
# rm transformed_application.yaml removes the temporary file

chatBTP ask -m 'please transform the following yaml input. It is a Helm file. i want to remove the two variables siteSubdomain siteDomain and replace them with a template. {{ include "site.subdomain" (dict "Values" .Values "siteName" "<name>" ) }}  replace "name". The value of replacing name, you find in the declaration of the  siteSubdomain. It is the first arguments that goes into printf in the variable declaration, without a trailing -.Do the same for the seiteWebComponentDomain  Remove the unused variables from the yaml. Please answer in yaml, do not add any extra information besides the yaml, i want to pipe the output in a .yaml file. Here is your input:' --file ui-application.yaml -a > transformed_application.yaml && mv transformed_application.yaml ui-application.yaml && rm transformed_application.yaml
