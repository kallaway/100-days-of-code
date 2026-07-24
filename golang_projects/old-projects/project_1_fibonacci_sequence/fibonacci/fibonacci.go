package fibonacci

// Fibonacci Sequence
// 1, 1, 2, 3, 5, 8, 13, 21, ...
// A(n) = A(n-1) + A(n-2) with A(0) = 1 A(1) = 1

type Sequence []uint

func (s *Sequence) FibonacciElement(initialPosition int) uint {
	if initialPosition > len(*s) {
		s.fibonacciSequenceIncrement(initialPosition)
	}
	return (*s)[initialPosition-1]
}

func (s *Sequence) FibonacciPartialSequence(initialPosition, finalPosition int) []uint {
	if finalPosition > len(*s) {
		s.fibonacciSequenceIncrement(finalPosition)
	}
	if initialPosition > len(*s) {
		s.fibonacciSequenceIncrement(initialPosition)
		return (*s)[initialPosition-1:]
	}
	return (*s)[initialPosition-1 : finalPosition]
}

func (s *Sequence) fibonacciSequenceIncrement(position int) {
	for i := len(*s) - 1; i < position-1; i++ {
		nextSequenceElement := (*s)[i] + (*s)[i-1]
		*s = append(*s, nextSequenceElement)
	}
}

func (s *Sequence) EntireSequence() []uint {
	return (*s)[:]
}

func (s *Sequence) fibonacciSequenceInitializer() {
	*s = append(*s, 1, 1)
}

func SequenceInitializer() Sequence {
	s := make(Sequence, 0)
	s.fibonacciSequenceInitializer()
	return s
}
