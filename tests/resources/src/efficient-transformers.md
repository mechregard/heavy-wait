## Discussion on efficient transformers paper
multi-headed self-attention mechanism for learning alignment scores between tokens. The attention, or value, is the 'porportional' bits of the encoder key values (the query is the decoder). self-attention because unsupervised (learn a representation of the sequence)
previous value (decoder Query) used to predict next (from this decoder and input key/value)
value is scaled output of the dot product of the query with all the keys (orthogonal vectors)

Efficient models

The primary goal of most of these models, with the exception of those based on segment-based recurrence, is to approximate the 
quadratic-cost attention matrix.

Fixed Patterns: Limit field of view like pooling
Combination of Patterns: Combine different pattern techniques
Learnable Patterns: learn above patterns- one example is combining similar tokens to single bucket. This clustering is learned. this class of methods learn to sort/cluster the input tokens - enabling a more optimal global view of the sequence while maintaining the efficiency benefits of fixed patterns approaches
Memory: Access input tokens by external memory. perform a preliminary pooling like operation of the input sequence to compress the input sequence
Low Rank: use low-rank approx of the self-attention NxN matrix. Linformer projects key/value to lower dim representation.
Kernal: rewrite the self-attention matrix to avoid NxN computation (similar to low rank)
Recurrence: like fixed patterns, where the pattern blocks are combined

Linear Transformer (Katharopoulos et al., 2020) is promising kernal method

Fast Attention via Orthogonal Random Features (FAVOR) The above computa- tion is still quadratic in complexity. Hence, the Performer leverages approximation tricks to avoid storing and computing the N × N attention matrix. It leverages orthogonal random features (ORF) for doing so

