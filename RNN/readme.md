
# RNN <br>
  1) What is RNN
  2) Hidden State (Memory Cell)
  3) Long Short-Time Memory(LSTM)

## 1. What is RNN? ##
  #### *Recurrent Neural Network(RNN)*
  
  * RNN이란 순환 신경망 구조라고 한다.<br>
  * RNN은 시간의 연속(Total time is 'T')으로 구성된 데이터를 차례대로 입력받고, 입력된 데이터로부터 T시간 이후의 데이터의 대해 어떤 결과를 추측하거나 생성해주는 것이 RNN이다.<br>
    
  #### *RNN Architecture*
  ![alt Text](https://github.com/oryondark/-/blob/master/RNN/RNN_unfold.png)

## 2. Hidden State
  #### *What is Hidden-State?*
  
  * Hidden State란 RNN에서 입력된 데이터를 기억하기 위한 기능이다.
  * Hidden State가 어떻게 동작하는 지, 그 구조를 이해해야 비로서 RNN의 구조를 이해하고, 완벽하게 사용할 수 있을 것이다.
  * 기존의 RNN은 바로 이 Hidden State 하나에 의존하는 것에 사람의 뇌와 같은 역할을 수행할 수 있다고 여겨졌다. 그러나, 기존의 활성화 뉴런의 활성함수가 배니싱(Vanishing)이라는 문제를 발생시키기 때문에, 일정 시간이 지난 뒤에는 학습률이 도저히 올라가지 않는 문제점이 발생하게 된다.
  * 따라서 이를 해결하기 위해 LSTM이라는 Hidden State 하나에 의존하지 않는 새로운 학습 메모리 셀이 등장하였으며, 자연어 처리 등을 포함한 실제 우리가 원하는 인공지능적인 문제를 해결하기 위한 모델로서 많이 활용되고 있다.
  * 다음 홍공 과학대에서 발표한 논문을 통해 RNN의 모델이 어떻게 학습하는지, Hidden-State를 분석한 내용을 살펴 볼 수 있다.
  * Understanding Hidden Memories of Recurrent Neural Networks<br>
    Yao Ming * Shaozu Cao * Ruixiang Zhang * Zhen Li * Yuanzhe Chen *
    Yangqiu Song, Member, IEEE * Huamin Qu, Member, IEEE *
    
  * 
