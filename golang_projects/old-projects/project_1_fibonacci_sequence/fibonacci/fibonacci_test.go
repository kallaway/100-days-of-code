package fibonacci

import (
	"reflect"
	"testing"
)

func TestSequenceInitializer(t *testing.T) {
	tests := []struct {
		name string
		want Sequence
	}{
		{
			name: "Validate sequence initialization.",
			want: Sequence{1, 1},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := SequenceInitializer(); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("SequenceInitializer() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestSequence_EntireSequence(t *testing.T) {
	tests := []struct {
		name string
		s    Sequence
		want []uint
	}{
		{
			name: "Validate if the entire sequence is passed",
			s:    Sequence{1, 1, 2, 3, 5, 8},
			want: []uint{1, 1, 2, 3, 5, 8},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.s.EntireSequence(); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("EntireSequence() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestSequence_FibonacciElement(t *testing.T) {
	type args struct {
		initialPosition int
	}
	tests := []struct {
		name string
		s    Sequence
		args args
		want uint
	}{
		{
			name: "Valid position",
			s:    Sequence{1, 1},
			args: args{
				initialPosition: 5,
			},
			want: uint(5),
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.s.FibonacciElement(tt.args.initialPosition); got != tt.want {
				t.Errorf("FibonacciElement() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestSequence_FibonacciPartialSequence(t *testing.T) {
	type args struct {
		initialPosition int
		finalPosition   int
	}
	tests := []struct {
		name string
		s    Sequence
		args args
		want []uint
	}{
		{
			name: "Valid interval",
			s:    Sequence{1, 1},
			args: args{
				initialPosition: 3,
				finalPosition:   5,
			},
			want: []uint{2, 3, 5},
		},
		{
			name: "finalPosition zero",
			s:    Sequence{1, 1},
			args: args{
				initialPosition: 3,
				finalPosition:   0,
			},
			want: []uint{2},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.s.FibonacciPartialSequence(tt.args.initialPosition, tt.args.finalPosition); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("FibonacciPartialSequence() = %v, want %v", got, tt.want)
			}
		})
	}
}
