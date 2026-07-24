package handlers

import (
	"testing"
)

func TestPositions_InputHandler(t *testing.T) {
	type fields struct {
		InitialPosition int
		FinalPosition   int
	}
	tests := []struct {
		name    string
		fields  fields
		wantErr bool
	}{
		{
			name: "Valid input",
			fields: fields{
				InitialPosition: 75,
				FinalPosition:   84,
			},
			wantErr: false,
		},
		{
			name: "Valid input with final position zero",
			fields: fields{
				InitialPosition: 5,
				FinalPosition:   0,
			},
			wantErr: false,
		},
		{
			name: "Invalid input with final position negative",
			fields: fields{
				InitialPosition: 5,
				FinalPosition:   -1,
			},
			wantErr: true,
		},
		{
			name: "Invalid input with initial position negative",
			fields: fields{
				InitialPosition: -1,
				FinalPosition:   -1,
			},
			wantErr: true,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			p := &Positions{
				InitialPosition: tt.fields.InitialPosition,
				FinalPosition:   tt.fields.FinalPosition,
			}
			if err := p.InputHandler(); (err != nil) != tt.wantErr {
				t.Errorf("InputHandler() error = %v, wantErr %v", err, tt.wantErr)
			}
		})
	}
}
