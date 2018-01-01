import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatButtonModule, MatToolbarModule, MatCardModule, MatInputModule, MatSidenavModule, MatListModule  } from '@angular/material';

@NgModule({
  imports: [ MatButtonModule, MatToolbarModule, MatCardModule, MatInputModule, MatSidenavModule, MatListModule ],
  exports: [ MatButtonModule, MatToolbarModule, MatCardModule, MatInputModule, MatSidenavModule, MatListModule ],
})
export class MaterialModule { }
