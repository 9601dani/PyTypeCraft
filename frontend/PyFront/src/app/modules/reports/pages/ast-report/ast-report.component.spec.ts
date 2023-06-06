import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AstReportComponent } from './ast-report.component';

describe('AstReportComponent', () => {
  let component: AstReportComponent;
  let fixture: ComponentFixture<AstReportComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AstReportComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AstReportComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
