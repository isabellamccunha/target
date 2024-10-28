# Interruptores e Lâmpadas - Teste Técnico

Este arquivo explica a estratégia para identificar qual interruptor controla cada lâmpada.

## Estratégia de Solução

1. **Ligue o primeiro interruptor** e deixe-o ligado por alguns minutos.
2. **Desligue o primeiro interruptor** e ligue o segundo imediatamente antes de entrar na sala das lâmpadas.
3. **Vá até a sala das lâmpadas** e verifique o estado de cada uma:
   - A lâmpada que estiver acesa está conectada ao **segundo interruptor** (que está ligado no momento).
   - A lâmpada que estiver apagada mas quente está conectada ao **primeiro interruptor** (que foi ligado e depois desligado).
   - A lâmpada que estiver apagada e fria está conectada ao **terceiro interruptor** (que nunca foi ligado).
