# Annotation Schema — Overview

## Introduction
The annotation schema is based on [Qiu (2013)] and comprises 69 semantic-functional sentence types.

## Annotation Levels
### Level 1: Sentence-level Classification
- Labeling each sentence as one of 69 functional types

### Level 2: Intra-sentence Role Labeling
- According to the semantic function, the sentence is divided into two parts and labeled according to the semantic function.


## Annotation Examples with English Translation

| Category Code | Type | Chinese Example | English Translation | Structure |
|--------------|------|-----------------|--------------------- |-------|------------------|-----------|----------|
| ENT       | 性质句  | Topic or entity being discussed | 日常生活中阿萨德【T当事/有生】\|\|也非常乐于助人【C性质】。 | In his daily life【T Party/Living】\|\|, Assad also very helpful【C Nature】| [T-Party/living + C-Nature] |
| ST        | 状态句  | Stative clause describing condition | 非洲超6亿人【T当事/有生】\|\|生活在无电可用的环境中【C状态】 | Over 600 million people in Africa 【T Party/Existence】\|\| live without access to electricity 【C State】| [T-Party/Existence + C-State] |
| QTY       | 量事句  | Quantitative information clause | 前4个月双边贸易额【T量事】\|\|即突破400亿美元【C计价】 | Bilateral trade volume in the first four months 【T-volume】 | | exceeded US$40 billion 【C-currency】| [T-volume + C-currency] |
| CAUSE     | 致事句  | Causative/Result clause | 在中乌共同努力下【T致事】\|\|，后续工程会按期投产【C结果】 | Through the joint efforts of China and Uzbekistan【T Commitment】\|\|, the subsequent projects will be put into operation on schedule【C Outcome】| [T-Commitment + C-Outcome] |
| EVAL      | 评价句  | Evaluative/judgment clause | 想在这里修建电站【T评事】\|\|并非易事【C所评/难易】 | uilding a power station here【T Comment】 \ | is no easy task【C Comment/Difficulty】|  [T-Comment + C-Difficulty] |
| Change    | 所变句  | 中海合作的效应【T所变】\|\|正不断注入新的时代内涵【C致变】 | China-sea cooperation effects【T-Changed】\|\|are continuously being infused with new contemporary implications【C-Change】 | [T-Changed + C-Change] |
| Statement | 断事句  | 中国【T断事】\|\|是应对气候变化、推动节能减排的表率【C所断】 | China【T-Subject】\|\|is a model for addressing climate change and promoting energy conservation【C-Statement】 | [T-Subject + C-Statement] |
| Metaphor  | 所喻句  | 中阿两大民族【T喻事】\|\|虽相隔遥远，却亲如一家【C所喻】 | The Chinese and Arab nations【T-Compare】\|\|though geographically distant, are as close as family【C-Metaphor】 | [T-Compare + C-Metaphor] |

## Annotation Format
- Sentence pattern markers: Use curly braces {...}
- Component boundaries: Use double vertical bars ||
- Semantic roles: Use square brackets 【...】

## Note
-  Each sentence must be fully annotated at three levels: sentence pattern, topic component, and subject-predicate components.
- The English translations serve academic documentation purposes while maintaining the original Chinese annotation structure.

## Copyright Notice
Due to copyright measures, the complete labeling schema is not publicly available. Only representative examples are provided for reference.

## References
Qiu, X. (2013). 汉语话说结构句法学 [The Theory of Topic-Comment Structure Syntax]. Beijing: World Book Publishing Company.