#!/bin/bash
if [ "$#" -lt 2 ]; then
  echo "Ошибка: недостаток входящих данных."
  exit 1
fi

GENE_NAME=$1
EXPRESSION_LEVEL=$2

echo "Экспрессия гена $GENE_NAME составляет $EXPRESSION_LEVEL единиц"
