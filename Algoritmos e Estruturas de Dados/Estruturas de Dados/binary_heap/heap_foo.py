#min-heap: o valor de cada nó é maior ou igual do que o do seu pai
#logo, o menor valor esta na raiz

#max-heap: o valor de cada nó é menor ou igual do que o do seu pai
#logo, o maior valor esta na raiz

#Os elementos estão dispostos na heap de forma que o pai sempre tem prioridade maior
#ou igual do que a prioridade de seus filhos.

#cada posição do array é considerado pai de outras duas posições que sao os filhos

#A posicao "i" passa a ser pai das posicoes:
# 2i + 1 (filho a esquerda)
# 2i + 2 (filho a direita)

#index 0,1,2
#ex: [2,5,7]

#index 0 é pai do index 1 do e index 2
# 2*0+1 = 1; 2*0+2 = 2;

#o array sempre ficara ordenado de acordo com a propriedade que esta heap assumir