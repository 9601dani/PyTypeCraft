import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CstReportComponent } from './cst-report.component';

describe('CstReportComponent', () => {
  let component: CstReportComponent;
  let fixture: ComponentFixture<CstReportComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CstReportComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CstReportComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
