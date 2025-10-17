# XML

```
<?xml version="1.0" encoding="Windows-1252"?>
<?FormVersion 6.0?>
<?FormSize 107:11?>
<Form>
  <Cmpnt Type="EACSFComponents*.ACSFForm" Name="RootComponent">
    <Prps>
      <Prp Name="Title text">Surgery Operative Risk Score</Prp>
      <Prp Name="Flowsheet template">647
PH T IP SUR PREOP RISK
647</Prp>
      <Prp Name="Title style">2</Prp>
      <Prp Name="Wrap captions">True</Prp>
      <Prp Name="Show title button">False</Prp>
      <Prp Name="Width">73%</Prp>
      <Prp Name="Title font">;;;;False;False;</Prp>
      <Prp Name="Use theming">1</Prp>
    </Prps>
    <Chld>
      <Cmpnt Type="EACSFComponents*.ACSFTableRow" Name="Row6">
        <Prps>
          <Prp Name="Rows">1</Prp>
          <Prp Name="Columns">1</Prp>
        </Prps>
        <Chld>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell7" DSrc="3" DFld="1" DCnt="1" DTyp="6">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Cell row">1</Prp>
              <Prp Name="Prompt">ASA Class</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFList" Name="Choice1ASA" DSrc="3" DFld="2" DCnt="1" DTyp="6">
                <Prps>
                  <Prp Name="ListSource">3</Prp>
                  <Prp Name="Choices">Healthy patient, no disease outside surgical process;Mild to moderate systemic disease, medically well controlled, with no functional limitation;Severe systemic disease that results in functional limitation;Severe incapacitating disease process that is a constant threat to life;Moribund patient not expected to survive 24 hours without an operation</Prp>
                  <Prp Name="ListCUI">15988</Prp>
                  <Prp Name="Multiple select">False</Prp>
                  <Prp Name="Tooltip text">Healthy patient, no disease outside surgical process=1;Mild to moderate systemic disease, medically well controlled, with no functional limitation=2;Severe systemic disease that results in functional limitation=3;Severe incapacitating disease process that is a constant threat to life=4;Moribund patient not expected to survive 24 hours without an operation=5</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
        </Chld>
      </Cmpnt>
      <Cmpnt Type="EACSFComponents*.ACSFTableRow" Name="Row8">
        <Prps>
          <Prp Name="Rows">1</Prp>
          <Prp Name="Columns">1</Prp>
        </Prps>
        <Chld>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell9" DSrc="3" DFld="3" DCnt="1" DTyp="6">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Cell row">1</Prp>
              <Prp Name="Prompt">Functional Status</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFList" Name="Choice2Function" DSrc="3" DFld="4" DCnt="1" DTyp="6">
                <Prps>
                  <Prp Name="ListSource">3</Prp>
                  <Prp Name="Choices">Independent;Partially Independent;Totally Dependent</Prp>
                  <Prp Name="ListCUI">15989</Prp>
                  <Prp Name="Multiple select">False</Prp>
                  <Prp Name="Tooltip text">Independent=1;Partially Independent=2;Totally Dependent=3</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
        </Chld>
      </Cmpnt>
      <Cmpnt Type="EACSFComponents*.ACSFTableRow" Name="Row9">
        <Prps>
          <Prp Name="Rows">1</Prp>
          <Prp Name="Columns">1</Prp>
        </Prps>
        <Chld>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell10" DSrc="3" DFld="5" DCnt="1" DTyp="6">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Cell row">1</Prp>
              <Prp Name="Prompt">Emergency</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFList" Name="Choice3Emergency" DSrc="3" DFld="6" DCnt="1" DTyp="6">
                <Prps>
                  <Prp Name="ListSource">3</Prp>
                  <Prp Name="Choices">Yes;No</Prp>
                  <Prp Name="ListCUI">15995</Prp>
                  <Prp Name="Multiple select">False</Prp>
                  <Prp Name="Tooltip text">Yes=2;No=1</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
        </Chld>
      </Cmpnt>
      <Cmpnt Type="EACSFComponents*.ACSFTableRow" Name="Row10">
        <Prps>
          <Prp Name="Rows">1</Prp>
          <Prp Name="Columns">1</Prp>
        </Prps>
        <Chld>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell11" DSrc="3" DFld="7" DCnt="1" DTyp="6">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Cell row">1</Prp>
              <Prp Name="Prompt">Smoking (in Last Year)</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFList" Name="Choice4Smoking" DSrc="3" DFld="8" DCnt="1" DTyp="6">
                <Prps>
                  <Prp Name="ListSource">3</Prp>
                  <Prp Name="Choices">Yes;No</Prp>
                  <Prp Name="ListCUI">15992</Prp>
                  <Prp Name="Multiple select">False</Prp>
                  <Prp Name="Tooltip text">Yes=2;No=1</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
        </Chld>
      </Cmpnt>
      <Cmpnt Type="EACSFComponents*.ACSFTableRow" Name="Row11">
        <Prps>
          <Prp Name="Rows">1</Prp>
          <Prp Name="Columns">1</Prp>
        </Prps>
        <Chld>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell12" DSrc="3" DFld="9" DCnt="1" DTyp="6">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Cell row">1</Prp>
              <Prp Name="Prompt">Sepsis</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFList" Name="Choice5Sepsis" DSrc="3" DFld="10" DCnt="1" DTyp="6">
                <Prps>
                  <Prp Name="ListSource">3</Prp>
                  <Prp Name="Choices">None;Preoperative SIRS;Preoperative Sepsis;Preoperative Septic Shock</Prp>
                  <Prp Name="ListCUI">15890</Prp>
                  <Prp Name="Multiple select">False</Prp>
                  <Prp Name="Tooltip text">None=4;Preoperative SIRS=1;Preoperative Sepsis=2;Preoperative Septic Shock=3</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
        </Chld>
      </Cmpnt>
      <Cmpnt Type="EACSFComponents*.ACSFTableRow" Name="Row12">
        <Prps>
          <Prp Name="Rows">1</Prp>
          <Prp Name="Columns">1</Prp>
        </Prps>
        <Chld>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell13" DSrc="3" DFld="11" DCnt="1" DTyp="6">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Cell row">1</Prp>
              <Prp Name="Prompt">COPD</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFList" Name="Choice6COPD" DSrc="3" DFld="12" DCnt="1" DTyp="6">
                <Prps>
                  <Prp Name="ListSource">3</Prp>
                  <Prp Name="Choices">Yes;No</Prp>
                  <Prp Name="ListCUI">15994</Prp>
                  <Prp Name="Multiple select">False</Prp>
                  <Prp Name="Tooltip text">Yes=2;No=1</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
        </Chld>
      </Cmpnt>
      <Cmpnt Type="EACSFComponents*.ACSFTableRow" Name="Row13">
        <Prps>
          <Prp Name="Rows">1</Prp>
          <Prp Name="Columns">1</Prp>
        </Prps>
        <Chld>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell14" DSrc="3" DFld="13" DCnt="1" DTyp="6">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Visible">False</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Cell row">1</Prp>
              <Prp Name="Prompt">Type of Surgery</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFList" Name="Choice7SurgeryType" DSrc="3" DFld="14" DCnt="1" DTyp="6">
                <Prps>
                  <Prp Name="ListSource">3</Prp>
                  <Prp Name="Choices">Anorectal;Aortic;Bariatric;Brain;Breast;Cardiac;ENT;HPB;Gallbladder, appendix, adrenals, or spleen;Hernia (ventral,inguinal,femoral);Intestinal;Neck;OBGYN;Ortho;Other Abdomen;Peripheral Vascular;Skin;Spine;Non-esophageal thoracic;Vein;Urology</Prp>
                  <Prp Name="ListCUI">15993</Prp>
                  <Prp Name="Multiple select">False</Prp>
                  <Prp Name="Style">1</Prp>
                  <Prp Name="Tooltip text">Anorectal=1;Aortic=2;Bariatric=3;Brain=4;Breast=5;Cardiac=6;ENT=7;HPB=8;Gallbladder, appendix, adrenals, or spleen=9;Hernia (ventral,inguinal,femoral)=10;Intestinal=11;Neck=12;OBGYN=13;Ortho=14;Other Abdomen=15;Peripheral Vascular=16;Skin=17;Spine=18;Non-esophageal thoracic=19;Vein=20;Urology=21</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
        </Chld>
      </Cmpnt>
      <Cmpnt Type="EACSFComponents*.ACSFTableRow" Name="Row0">
        <Prps>
          <Prp Name="Rows">1</Prp>
          <Prp Name="Columns">1</Prp>
        </Prps>
        <Chld>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell0" DSrc="3" DFld="15" DCnt="1" DTyp="6">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Cell row">1</Prp>
              <Prp Name="Prompt">Type of Surgery</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFList" Name="Choice8SurgeryQuick" DSrc="3" DFld="16" DCnt="1" DTyp="6">
                <Prps>
                  <Prp Name="ListSource">3</Prp>
                  <Prp Name="Choices">Anorectal;Aortic;Bariatric;Brain;Breast;Cardiac;ENT;HPB;Gallbladder, appendix, adrenals, or spleen;Hernia (ventral,inguinal,femoral);Intestinal;Neck;OBGYN;Ortho;Other Abdomen;Peripheral Vascular;Skin;Spine;Non-esophageal thoracic;Vein;Urology</Prp>
                  <Prp Name="ListCUI">15993</Prp>
                  <Prp Name="Hidden responses">1;1;1;1;1;0;1;1;0;0;0;1;1;0;1;1;0;0;1;1;1</Prp>
                  <Prp Name="Multiple select">False</Prp>
                  <Prp Name="Tooltip text">Anorectal=1;Aortic=2;Bariatric=3;Brain=4;Breast=5;Cardiac=6;ENT=7;HPB=8;Gallbladder, appendix, adrenals, or spleen=9;Hernia (ventral,inguinal,femoral)=10;Intestinal=11;Neck=12;OBGYN=13;Ortho=14;Other Abdomen=15;Peripheral Vascular=16;Skin=17;Spine=18;Non-esophageal thoracic=19;Vein=20;Urology=21</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
        </Chld>
      </Cmpnt>
      <Cmpnt Type="EACSFComponents*.ACSFTableRow" Name="Row14">
        <Prps>
          <Prp Name="Rows">1</Prp>
          <Prp Name="Columns">4</Prp>
        </Prps>
        <Chld>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell15">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Width">25%</Prp>
              <Prp Name="Cell row">1</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFLabel" Name="Label0">
                <Prps>
                  <Prp Name="Caption">Risk Scores</Prp>
                  <Prp Name="Label type">1</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell25">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Width">25%</Prp>
              <Prp Name="Cell row">1</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFSpacer" Name="Spacer1" />
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell24">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Width">25%</Prp>
              <Prp Name="Cell row">1</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFLabel" Name="Label16">
                <Prps>
                  <Prp Name="Caption">Percentile Risk</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell26">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Width">25%</Prp>
              <Prp Name="Cell row">1</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFSpacer" Name="Spacer2" />
            </Chld>
          </Cmpnt>
        </Chld>
      </Cmpnt>
      <Cmpnt Type="EACSFComponents*.ACSFTableRow" Name="Row15">
        <Prps>
          <Prp Name="Rows">3</Prp>
          <Prp Name="Columns">7</Prp>
        </Prps>
        <Chld>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell38">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">20px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Width">23%</Prp>
              <Prp Name="Cell row">1</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFLabel" Name="Label5">
                <Prps>
                  <Prp Name="Font">Arial;12pt;bold;normal;false;false;#000000</Prp>
                  <Prp Name="Caption">Risk for Myocardial Infarction or Cardiac Arrest (MICA)</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell42">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Width">12%</Prp>
              <Prp Name="Cell row">1</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFSpacer" Name="Spacer27" />
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell19">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Width">9.2%</Prp>
              <Prp Name="Cell row">1</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFTableRow" Name="Row20">
                <Prps>
                  <Prp Name="Rows">1</Prp>
                  <Prp Name="Columns">1</Prp>
                </Prps>
                <Chld>
                  <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell20" DSrc="3" DFld="17" DCnt="1" DTyp="0">
                    <Prps>
                      <Prp Name="Column span">1</Prp>
                      <Prp Name="Component indent">1px</Prp>
                      <Prp Name="Prompt indent">1px</Prp>
                      <Prp Name="Cell row">1</Prp>
                    </Prps>
                    <Chld>
                      <Cmpnt Type="EACSFComponents*.ACSFChrontrol" Name="CardiacRisk" DSrc="3" DFld="18" DCnt="1" DTyp="0">
                        <Prps>
                          <Prp Name="Enabled">False</Prp>
                          <Prp Name="Requirements">1</Prp>
                          <Prp Name="Field properties">EACSFControls*.ACSFChrontrolPPG</Prp>
                          <Prp Name="Allow negative values">0</Prp>
                          <Prp Name="PropertyPageData">Y~####1##########~G~16777215#0##~	~##~</Prp>
                          <Prp Name="PPG Has Entry Button Set">False</Prp>
                        </Prps>
                      </Cmpnt>
                    </Chld>
                  </Cmpnt>
                </Chld>
              </Cmpnt>
              <Cmpnt Type="EACSFComponents*.ACSFTableRow" Name="Row21">
                <Prps>
                  <Prp Name="Rows">1</Prp>
                  <Prp Name="Columns">1</Prp>
                </Prps>
                <Chld>
                  <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell16">
                    <Prps>
                      <Prp Name="Column span">1</Prp>
                      <Prp Name="Component indent">1px</Prp>
                      <Prp Name="Prompt indent">1px</Prp>
                      <Prp Name="Width">50%</Prp>
                      <Prp Name="Cell row">1</Prp>
                    </Prps>
                    <Chld>
                      <Cmpnt Type="EACSFComponents*.ACSFTableRow" Name="Row19">
                        <Prps>
                          <Prp Name="Rows">1</Prp>
                          <Prp Name="Columns">1</Prp>
                        </Prps>
                        <Chld>
                          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell21">
                            <Prps>
                              <Prp Name="Column span">1</Prp>
                              <Prp Name="Visible">False</Prp>
                              <Prp Name="Component indent">1px</Prp>
                              <Prp Name="Prompt indent">1px</Prp>
                              <Prp Name="Cell row">1</Prp>
                            </Prps>
                            <Chld>
                              <Cmpnt Type="EACSFComponents*.ACSFLabel" Name="Label17">
                                <Prps>
                                  <Prp Name="Caption">High Risk (&gt;1%)</Prp>
                                  <Prp Name="Label type">8</Prp>
                                </Prps>
                              </Cmpnt>
                            </Chld>
                          </Cmpnt>
                        </Chld>
                      </Cmpnt>
                      <Cmpnt Type="EACSFComponents*.ACSFTableRow" Name="Row22">
                        <Prps>
                          <Prp Name="Rows">1</Prp>
                          <Prp Name="Columns">1</Prp>
                        </Prps>
                        <Chld>
                          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell23">
                            <Prps>
                              <Prp Name="Column span">1</Prp>
                              <Prp Name="Visible">False</Prp>
                              <Prp Name="Component indent">1px</Prp>
                              <Prp Name="Prompt indent">1px</Prp>
                              <Prp Name="Cell row">1</Prp>
                            </Prps>
                            <Chld>
                              <Cmpnt Type="EACSFComponents*.ACSFLabel" Name="Label18">
                                <Prps>
                                  <Prp Name="Tooltip text">No Further Workup Indicated</Prp>
                                  <Prp Name="Caption">Low Risk (&lt;1%)</Prp>
                                </Prps>
                              </Cmpnt>
                            </Chld>
                          </Cmpnt>
                        </Chld>
                      </Cmpnt>
                    </Chld>
                  </Cmpnt>
                </Chld>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell44">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Width">6.5%</Prp>
              <Prp Name="Cell row">1</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFLabel" Name="Label4">
                <Prps>
                  <Prp Name="Caption">%</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell2">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Width">17.5%</Prp>
              <Prp Name="Cell row">1</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFTableRow" Name="Row1">
                <Prps>
                  <Prp Name="Rows">1</Prp>
                  <Prp Name="Columns">1</Prp>
                </Prps>
                <Chld>
                  <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell1">
                    <Prps>
                      <Prp Name="Column span">1</Prp>
                      <Prp Name="Visible">False</Prp>
                      <Prp Name="Component indent">1px</Prp>
                      <Prp Name="Prompt indent">1px</Prp>
                      <Prp Name="Cell row">1</Prp>
                    </Prps>
                    <Chld>
                      <Cmpnt Type="EACSFComponents*.ACSFLabel" Name="Label10">
                        <Prps>
                          <Prp Name="Caption">&lt;25th</Prp>
                        </Prps>
                      </Cmpnt>
                    </Chld>
                  </Cmpnt>
                </Chld>
              </Cmpnt>
              <Cmpnt Type="EACSFComponents*.ACSFTableRow" Name="Row5">
                <Prps>
                  <Prp Name="Rows">1</Prp>
                  <Prp Name="Columns">1</Prp>
                </Prps>
                <Chld>
                  <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell4">
                    <Prps>
                      <Prp Name="Column span">1</Prp>
                      <Prp Name="Component indent">1px</Prp>
                      <Prp Name="Prompt indent">1px</Prp>
                      <Prp Name="Cell row">1</Prp>
                    </Prps>
                    <Chld>
                      <Cmpnt Type="EACSFComponents*.ACSFTableRow" Name="Row7">
                        <Prps>
                          <Prp Name="Rows">1</Prp>
                          <Prp Name="Columns">1</Prp>
                        </Prps>
                        <Chld>
                          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell3">
                            <Prps>
                              <Prp Name="Column span">1</Prp>
                              <Prp Name="Visible">False</Prp>
                              <Prp Name="Component indent">1px</Prp>
                              <Prp Name="Prompt indent">1px</Prp>
                              <Prp Name="Cell row">1</Prp>
                            </Prps>
                            <Chld>
                              <Cmpnt Type="EACSFComponents*.ACSFLabel" Name="Label11">
                                <Prps>
                                  <Prp Name="Caption">26- 50th</Prp>
                                </Prps>
                              </Cmpnt>
                            </Chld>
                          </Cmpnt>
                        </Chld>
                      </Cmpnt>
                      <Cmpnt Type="EACSFComponents*.ACSFTableRow" Name="Row16">
                        <Prps>
                          <Prp Name="Rows">1</Prp>
                          <Prp Name="Columns">1</Prp>
                        </Prps>
                        <Chld>
                          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell6">
                            <Prps>
                              <Prp Name="Column span">1</Prp>
                              <Prp Name="Component indent">1px</Prp>
                              <Prp Name="Prompt indent">1px</Prp>
                              <Prp Name="Cell row">1</Prp>
                            </Prps>
                            <Chld>
                              <Cmpnt Type="EACSFComponents*.ACSFTableRow" Name="Row17">
                                <Prps>
                                  <Prp Name="Rows">1</Prp>
                                  <Prp Name="Columns">2</Prp>
                                </Prps>
                                <Chld>
                                  <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell17">
                                    <Prps>
                                      <Prp Name="Column span">1</Prp>
                                      <Prp Name="Visible">False</Prp>
                                      <Prp Name="Component indent">1px</Prp>
                                      <Prp Name="Prompt indent">1px</Prp>
                                      <Prp Name="Width">50%</Prp>
                                      <Prp Name="Cell row">1</Prp>
                                    </Prps>
                                    <Chld>
                                      <Cmpnt Type="EACSFComponents*.ACSFLabel" Name="Label12">
                                        <Prps>
                                          <Prp Name="Caption">51st - 90th</Prp>
                                        </Prps>
                                      </Cmpnt>
                                    </Chld>
                                  </Cmpnt>
                                  <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell18">
                                    <Prps>
                                      <Prp Name="Column span">1</Prp>
                                      <Prp Name="Visible">False</Prp>
                                      <Prp Name="Component indent">1px</Prp>
                                      <Prp Name="Prompt indent">1px</Prp>
                                      <Prp Name="Width">52%</Prp>
                                      <Prp Name="Cell row">1</Prp>
                                    </Prps>
                                    <Chld>
                                      <Cmpnt Type="EACSFComponents*.ACSFLabel" Name="Label15">
                                        <Prps>
                                          <Prp Name="Caption">91st - 95th</Prp>
                                        </Prps>
                                      </Cmpnt>
                                    </Chld>
                                  </Cmpnt>
                                </Chld>
                              </Cmpnt>
                              <Cmpnt Type="EACSFComponents*.ACSFTableRow" Name="Row18">
                                <Prps>
                                  <Prp Name="Rows">1</Prp>
                                  <Prp Name="Columns">2</Prp>
                                </Prps>
                                <Chld>
                                  <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell5">
                                    <Prps>
                                      <Prp Name="Column span">1</Prp>
                                      <Prp Name="Visible">False</Prp>
                                      <Prp Name="Component indent">1px</Prp>
                                      <Prp Name="Prompt indent">1px</Prp>
                                      <Prp Name="Width">67.8%</Prp>
                                      <Prp Name="Cell row">1</Prp>
                                    </Prps>
                                    <Chld>
                                      <Cmpnt Type="EACSFComponents*.ACSFLabel" Name="Label13">
                                        <Prps>
                                          <Prp Name="Caption">96-97th</Prp>
                                        </Prps>
                                      </Cmpnt>
                                    </Chld>
                                  </Cmpnt>
                                  <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell8">
                                    <Prps>
                                      <Prp Name="Column span">1</Prp>
                                      <Prp Name="Visible">False</Prp>
                                      <Prp Name="Component indent">1px</Prp>
                                      <Prp Name="Prompt indent">1px</Prp>
                                      <Prp Name="Width">32.2%</Prp>
                                      <Prp Name="Cell row">1</Prp>
                                    </Prps>
                                    <Chld>
                                      <Cmpnt Type="EACSFComponents*.ACSFLabel" Name="Label14">
                                        <Prps>
                                          <Prp Name="Caption">97th</Prp>
                                        </Prps>
                                      </Cmpnt>
                                    </Chld>
                                  </Cmpnt>
                                </Chld>
                              </Cmpnt>
                            </Chld>
                          </Cmpnt>
                        </Chld>
                      </Cmpnt>
                    </Chld>
                  </Cmpnt>
                </Chld>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell45" DSrc="3" DFld="19" DCnt="1" DTyp="2">
            <Prps>
              <Prp Name="Column span">2</Prp>
              <Prp Name="Visible">False</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Width">30%</Prp>
              <Prp Name="Cell row">1</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFChrontrol" Name="ASA" DSrc="3" DFld="20" DCnt="1" DTyp="2">
                <Prps>
                  <Prp Name="Enabled">False</Prp>
                  <Prp Name="Requirements">1</Prp>
                  <Prp Name="Field properties">EACSFControls*.ACSFChrontrolPPG</Prp>
                  <Prp Name="Allow negative values">0</Prp>
                  <Prp Name="PropertyPageData">N~#######~Y~####12##########~G~16777215###~	~##~</Prp>
                  <Prp Name="PPG Has Entry Button Set">True</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell51">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">20px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Width">23%</Prp>
              <Prp Name="Cell row">2</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFLabel" Name="Label6">
                <Prps>
                  <Prp Name="Font">Arial;12pt;bold;normal;false;false;#000000</Prp>
                  <Prp Name="Caption">Post-Op Respiratory Failure</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell54">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Width">12%</Prp>
              <Prp Name="Cell row">2</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFSpacer" Name="Spacer37" />
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell50" DSrc="3" DFld="21" DCnt="1" DTyp="0">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Width">9.2%</Prp>
              <Prp Name="Cell row">2</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFChrontrol" Name="PostOpRF" DSrc="3" DFld="22" DCnt="1" DTyp="0">
                <Prps>
                  <Prp Name="Enabled">False</Prp>
                  <Prp Name="Requirements">1</Prp>
                  <Prp Name="Field properties">EACSFControls*.ACSFChrontrolPPG</Prp>
                  <Prp Name="Allow negative values">0</Prp>
                  <Prp Name="PropertyPageData">Y~####1##########~G~16777215#0##~	~##~</Prp>
                  <Prp Name="PPG Has Entry Button Set">False</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell65">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Width">6.5%</Prp>
              <Prp Name="Cell row">2</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFLabel" Name="Label8">
                <Prps>
                  <Prp Name="Caption">%</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell56">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Width">17.5%</Prp>
              <Prp Name="Cell row">2</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFSpacer" Name="Spacer39" />
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell29">
            <Prps>
              <Prp Name="Column span">2</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Width">30%</Prp>
              <Prp Name="Cell row">2</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFSpacer" Name="Spacer18" />
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell60">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">20px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Width">23%</Prp>
              <Prp Name="Cell row">3</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFLabel" Name="Label7">
                <Prps>
                  <Prp Name="Font">Arial;12pt;bold;normal;false;false;#000000</Prp>
                  <Prp Name="Caption">Post-Op Pneumonia</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell63">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Width">12%</Prp>
              <Prp Name="Cell row">3</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFSpacer" Name="Spacer46" />
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell22" DSrc="3" DFld="23" DCnt="1" DTyp="0">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Width">9.2%</Prp>
              <Prp Name="Cell row">3</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFChrontrol" Name="PostOpPna" DSrc="3" DFld="24" DCnt="1" DTyp="0">
                <Prps>
                  <Prp Name="Enabled">False</Prp>
                  <Prp Name="Requirements">1</Prp>
                  <Prp Name="Field properties">EACSFControls*.ACSFChrontrolPPG</Prp>
                  <Prp Name="Allow negative values">0</Prp>
                  <Prp Name="PropertyPageData">Y~####1##########~G~16777215#0##~	~##~</Prp>
                  <Prp Name="PPG Has Entry Button Set">False</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell66">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Width">6.5%</Prp>
              <Prp Name="Cell row">3</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFLabel" Name="Label9">
                <Prps>
                  <Prp Name="Caption">%</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell31">
            <Prps>
              <Prp Name="Column span">3</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Width">47.5%</Prp>
              <Prp Name="Cell row">3</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFSpacer" Name="Spacer20" />
            </Chld>
          </Cmpnt>
        </Chld>
      </Cmpnt>
      <Cmpnt Type="EACSFComponents*.ACSFTableRow" Name="Row2">
        <Prps>
          <Prp Name="Rows">1</Prp>
          <Prp Name="Columns">1</Prp>
        </Prps>
        <Chld>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell32">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Cell row">1</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFLabel" Name="Label1">
                <Prps>
                  <Prp Name="Caption">Gupta PK, Gupta H, Sundaram A, et al. Development and validation of a risk calculator for prediction of cardiac risk after surgery. Circulation. 2011;124(4):381-7.</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
        </Chld>
      </Cmpnt>
      <Cmpnt Type="EACSFComponents*.ACSFTableRow" Name="Row3">
        <Prps>
          <Prp Name="Rows">1</Prp>
          <Prp Name="Columns">1</Prp>
        </Prps>
        <Chld>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell34">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Cell row">1</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFLabel" Name="Label2">
                <Prps>
                  <Prp Name="Caption">Gupta H, Gupta PK, Fang X, et al. Development and validation of a risk calculator predicting postoperative respiratory failure. Chest. 2011;140(5):1207-1215.</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
        </Chld>
      </Cmpnt>
      <Cmpnt Type="EACSFComponents*.ACSFTableRow" Name="Row4">
        <Prps>
          <Prp Name="Rows">1</Prp>
          <Prp Name="Columns">1</Prp>
        </Prps>
        <Chld>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell35">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Cell row">1</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFLabel" Name="Label3">
                <Prps>
                  <Prp Name="Caption">Gupta H, Gupta PK, Schuller D, et al. Development and validation of a risk calculator for predicting postoperative pneumonia. Mayo Clin Proc. 2013;88(11):1241-9.</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
        </Chld>
      </Cmpnt>
    </Chld>
  </Cmpnt>
  <FormScripts ScriptVersion="1.0">
    <Script Name="Choice7SurgeryType_ValueChanged" ProcType="3" CreationType="2" ParamCount="0" Component="">
      <Action ActionType="1" Name="Choice7Visible" Key="Condition1">
        <ActionProperty Name="IfConnectionLogic" Value="1" />
        <Checks>
          <Check CheckType="1" Name="Choice7Visible" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckPropComponentID" Value="Choice7SurgeryType" />
            <CheckProperty Name="IfCheckPropRealComponentID" Value="Cell14" />
            <CheckProperty Name="IfCheckPropProperty" Value="Visible" />
            <CheckProperty Name="IfCheckPropValue" Value="True" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="4" Name="Choice8SurgeryVis" Key="Action1">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell0" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="Choice8SurgeryQuick" />
          </Action>
        </TrueBranch>
        <FalseBranch>
          <Action ActionType="4" Name="Choice8SurgeryVis" Key="Action2">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell0" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="Choice8SurgeryQuick" />
          </Action>
        </FalseBranch>
      </Action>
    </Script>
    <Script Name="Choice8SurgeryQuick_ValueChanged" ProcType="3" CreationType="2" ParamCount="0" Component="">
      <Action ActionType="1" Name="MoreOptions" Key="Condition1">
        <ActionProperty Name="IfConnectionLogicType" Value="2" />
        <ActionProperty Name="IfConnectionLogic" Value="(1 AND 2 AND 3 AND 4 AND 5 AND 6 AND 7)" />
        <Checks>
          <Check CheckType="2" Name="Cardiac" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="Choice8SurgeryQuick" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="Choice8SurgeryQuick" />
            <CheckProperty Name="IfCheckValueOperator" Value="2" />
            <CheckProperty Name="IfCheckValueValue" Value="Cardiac$$C6$$" />
          </Check>
          <Check CheckType="2" Name="GB" Key="Check2" CheckNum="2">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="Choice8SurgeryQuick" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="Choice8SurgeryQuick" />
            <CheckProperty Name="IfCheckValueOperator" Value="2" />
            <CheckProperty Name="IfCheckValueValue" Value="Gallbladder, appendix, adrenals, or spleen$$C6$$" />
          </Check>
          <Check CheckType="2" Name="Hernia" Key="Check3" CheckNum="3">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="Choice8SurgeryQuick" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="Choice8SurgeryQuick" />
            <CheckProperty Name="IfCheckValueOperator" Value="2" />
            <CheckProperty Name="IfCheckValueValue" Value="Hernia (ventral,inguinal,femoral)$$C6$$" />
          </Check>
          <Check CheckType="2" Name="Intestinal" Key="Check4" CheckNum="4">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="Choice8SurgeryQuick" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="Choice8SurgeryQuick" />
            <CheckProperty Name="IfCheckValueOperator" Value="2" />
            <CheckProperty Name="IfCheckValueValue" Value="Intestinal$$C6$$" />
          </Check>
          <Check CheckType="2" Name="Ortho" Key="Check5" CheckNum="5">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="Choice8SurgeryQuick" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="Choice8SurgeryQuick" />
            <CheckProperty Name="IfCheckValueOperator" Value="2" />
            <CheckProperty Name="IfCheckValueValue" Value="Ortho$$C6$$" />
          </Check>
          <Check CheckType="2" Name="Skin" Key="Check6" CheckNum="6">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="Choice8SurgeryQuick" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="Choice8SurgeryQuick" />
            <CheckProperty Name="IfCheckValueOperator" Value="2" />
            <CheckProperty Name="IfCheckValueValue" Value="Skin$$C6$$" />
          </Check>
          <Check CheckType="2" Name="Spine" Key="Check7" CheckNum="7">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="Choice8SurgeryQuick" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="Choice8SurgeryQuick" />
            <CheckProperty Name="IfCheckValueOperator" Value="2" />
            <CheckProperty Name="IfCheckValueValue" Value="Spine$$C6$$" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="4" Name="Choice7Visible" Key="Action1">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell14" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="Choice7SurgeryType" />
          </Action>
          <Action ActionType="4" Name="Choice8Visible" Key="Action3">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell0" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="Choice8SurgeryQuick" />
          </Action>
        </TrueBranch>
        <FalseBranch>
          <Action ActionType="4" Name="Choice7Visible" Key="Action2">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell14" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="Choice7SurgeryType" />
          </Action>
          <Action ActionType="4" Name="Choice8Visible" Key="Action4">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell0" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="Choice8SurgeryQuick" />
          </Action>
        </FalseBranch>
      </Action>
    </Script>
    <Script Name="RootComponent_AfterDataLoaded" ProcType="3" CreationType="2" ParamCount="0" Component="">
      <Action ActionType="1" Name="Load " Key="Condition1">
        <ActionProperty Name="IfConnectionLogic" Value="1" />
        <Checks>
          <Check CheckType="1" Name="Load" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckPropComponentID" Value="Choice1ASA" />
            <CheckProperty Name="IfCheckPropRealComponentID" Value="Cell7" />
            <CheckProperty Name="IfCheckPropProperty" Value="Visible" />
            <CheckProperty Name="IfCheckPropValue" Value="True" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="1" Name="Choice6COPD" Key="Condition3">
            <ActionProperty Name="IfConnectionLogic" Value="1" />
            <Checks>
              <Check CheckType="4" Name="SmokingRule" Key="Check1" CheckNum="1">
                <CheckProperty Name="IfCheckRuleID" Value="1" />
              </Check>
            </Checks>
            <TrueBranch>
              <Action ActionType="3" Name="Choice6COPD" Key="Action6">
                <ActionProperty Name="SetValueRealComponentID" Value="Choice6COPD" />
                <ActionProperty Name="SetValueWhich" Value="1" />
                <ActionProperty Name="SetValueComponentID" Value="Choice6COPD" />
                <ActionProperty Name="SetValueComponentValue" Value="Yes$$C6$$" />
              </Action>
            </TrueBranch>
            <FalseBranch>
              <Action ActionType="3" Name="Choice6COPD" Key="Action8">
                <ActionProperty Name="SetValueRealComponentID" Value="Choice6COPD" />
                <ActionProperty Name="SetValueWhich" Value="1" />
                <ActionProperty Name="SetValueComponentID" Value="Choice6COPD" />
                <ActionProperty Name="SetValueComponentValue" Value="No$$C6$$" />
              </Action>
            </FalseBranch>
          </Action>
          <Action ActionType="3" Name="Choice2Function" Key="Action2">
            <ActionProperty Name="SetValueRealComponentID" Value="Choice2Function" />
            <ActionProperty Name="SetValueWhich" Value="1" />
            <ActionProperty Name="SetValueComponentID" Value="Choice2Function" />
            <ActionProperty Name="SetValueComponentValue" Value="Independent$$C6$$" />
          </Action>
          <Action ActionType="3" Name="Choice3Emergency" Key="Action3">
            <ActionProperty Name="SetValueRealComponentID" Value="Choice3Emergency" />
            <ActionProperty Name="SetValueWhich" Value="1" />
            <ActionProperty Name="SetValueComponentID" Value="Choice3Emergency" />
            <ActionProperty Name="SetValueComponentValue" Value="No$$C6$$" />
          </Action>
          <Action ActionType="1" Name="Choice4Smoking" Key="Condition2">
            <ActionProperty Name="IfConnectionLogic" Value="1" />
            <Checks>
              <Check CheckType="4" Name="SmokingRule" Key="Check1" CheckNum="1">
                <CheckProperty Name="IfCheckRuleID" Value="2" />
              </Check>
            </Checks>
            <TrueBranch>
              <Action ActionType="3" Name="Choice4Smoking" Key="Action4">
                <ActionProperty Name="SetValueRealComponentID" Value="Choice4Smoking" />
                <ActionProperty Name="SetValueWhich" Value="1" />
                <ActionProperty Name="SetValueComponentID" Value="Choice4Smoking" />
                <ActionProperty Name="SetValueComponentValue" Value="Yes$$C6$$" />
              </Action>
            </TrueBranch>
            <FalseBranch>
              <Action ActionType="3" Name="Choice4Smoking" Key="Action5">
                <ActionProperty Name="SetValueRealComponentID" Value="Choice4Smoking" />
                <ActionProperty Name="SetValueWhich" Value="1" />
                <ActionProperty Name="SetValueComponentID" Value="Choice4Smoking" />
                <ActionProperty Name="SetValueComponentValue" Value="No$$C6$$" />
              </Action>
            </FalseBranch>
          </Action>
          <Action ActionType="1" Name="Choice5Sepsis" Key="Condition4">
            <ActionProperty Name="IfConnectionLogic" Value="1" />
            <Checks>
              <Check CheckType="4" Name="SIRS" Key="Check1" CheckNum="1">
                <CheckProperty Name="IfCheckRuleID" Value="3" />
              </Check>
            </Checks>
            <TrueBranch>
              <Action ActionType="3" Name="Choice4Smoking" Key="Action7">
                <ActionProperty Name="SetValueRealComponentID" Value="Choice5Sepsis" />
                <ActionProperty Name="SetValueWhich" Value="1" />
                <ActionProperty Name="SetValueComponentID" Value="Choice5Sepsis" />
                <ActionProperty Name="SetValueComponentValue" Value="Preoperative SIRS$$C6$$" />
              </Action>
            </TrueBranch>
            <FalseBranch>
              <Action ActionType="3" Name="Choice4Smoking" Key="Action9">
                <ActionProperty Name="SetValueRealComponentID" Value="Choice5Sepsis" />
                <ActionProperty Name="SetValueWhich" Value="1" />
                <ActionProperty Name="SetValueComponentID" Value="Choice5Sepsis" />
                <ActionProperty Name="SetValueComponentValue" Value="None$$C6$$" />
              </Action>
            </FalseBranch>
          </Action>
          <Action ActionType="1" Name="Choice1ASA" Key="Condition5">
            <ActionProperty Name="IfConnectionLogic" Value="1" />
            <Checks>
              <Check CheckType="2" Name="ASA5" Key="Check1" CheckNum="1">
                <CheckProperty Name="IfCheckValueWhich" Value="1" />
                <CheckProperty Name="IfCheckValueComponentID" Value="ASA" />
                <CheckProperty Name="IfCheckValueRealComponentID" Value="ASA" />
                <CheckProperty Name="IfCheckValueOperator" Value="1" />
                <CheckProperty Name="IfCheckValueValue" Value="5$$C6$$" />
              </Check>
            </Checks>
            <TrueBranch>
              <Action ActionType="3" Name="ASA5" Key="Action10">
                <ActionProperty Name="SetValueRealComponentID" Value="Choice1ASA" />
                <ActionProperty Name="SetValueWhich" Value="1" />
                <ActionProperty Name="SetValueComponentID" Value="Choice1ASA" />
                <ActionProperty Name="SetValueComponentValue" Value="Moribund patient not expected to survive 24 hours without an operation$$C6$$" />
              </Action>
            </TrueBranch>
            <FalseBranch>
              <Action ActionType="1" Name="ASA4" Key="Condition6">
                <ActionProperty Name="IfConnectionLogic" Value="1" />
                <Checks>
                  <Check CheckType="2" Name="ASA5" Key="Check1" CheckNum="1">
                    <CheckProperty Name="IfCheckValueWhich" Value="1" />
                    <CheckProperty Name="IfCheckValueComponentID" Value="ASA" />
                    <CheckProperty Name="IfCheckValueRealComponentID" Value="ASA" />
                    <CheckProperty Name="IfCheckValueOperator" Value="1" />
                    <CheckProperty Name="IfCheckValueValue" Value="4$$C6$$" />
                  </Check>
                </Checks>
                <TrueBranch>
                  <Action ActionType="3" Name="ASA4" Key="Action11">
                    <ActionProperty Name="SetValueRealComponentID" Value="Choice1ASA" />
                    <ActionProperty Name="SetValueWhich" Value="1" />
                    <ActionProperty Name="SetValueComponentID" Value="Choice1ASA" />
                    <ActionProperty Name="SetValueComponentValue" Value="Severe incapacitating disease process that is a constant threat to life$$C6$$" />
                  </Action>
                </TrueBranch>
                <FalseBranch>
                  <Action ActionType="1" Name="ASA3" Key="Condition7">
                    <ActionProperty Name="IfConnectionLogic" Value="1" />
                    <Checks>
                      <Check CheckType="2" Name="ASA5" Key="Check1" CheckNum="1">
                        <CheckProperty Name="IfCheckValueWhich" Value="1" />
                        <CheckProperty Name="IfCheckValueComponentID" Value="ASA" />
                        <CheckProperty Name="IfCheckValueRealComponentID" Value="ASA" />
                        <CheckProperty Name="IfCheckValueOperator" Value="1" />
                        <CheckProperty Name="IfCheckValueValue" Value="3$$C6$$" />
                      </Check>
                    </Checks>
                    <TrueBranch>
                      <Action ActionType="3" Name="ASA3" Key="Action13">
                        <ActionProperty Name="SetValueRealComponentID" Value="Choice1ASA" />
                        <ActionProperty Name="SetValueWhich" Value="1" />
                        <ActionProperty Name="SetValueComponentID" Value="Choice1ASA" />
                        <ActionProperty Name="SetValueComponentValue" Value="Severe systemic disease that results in functional limitation$$C6$$" />
                      </Action>
                    </TrueBranch>
                    <FalseBranch>
                      <Action ActionType="1" Name="ASA2" Key="Condition8">
                        <ActionProperty Name="IfConnectionLogic" Value="1" />
                        <Checks>
                          <Check CheckType="2" Name="ASA5" Key="Check1" CheckNum="1">
                            <CheckProperty Name="IfCheckValueWhich" Value="1" />
                            <CheckProperty Name="IfCheckValueComponentID" Value="ASA" />
                            <CheckProperty Name="IfCheckValueRealComponentID" Value="ASA" />
                            <CheckProperty Name="IfCheckValueOperator" Value="1" />
                            <CheckProperty Name="IfCheckValueValue" Value="2$$C6$$" />
                          </Check>
                        </Checks>
                        <TrueBranch>
                          <Action ActionType="3" Name="ASA2" Key="Action14">
                            <ActionProperty Name="SetValueRealComponentID" Value="Choice1ASA" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="Choice1ASA" />
                            <ActionProperty Name="SetValueComponentValue" Value="Mild to moderate systemic disease, medically well controlled, with no functional limitation$$C6$$" />
                          </Action>
                        </TrueBranch>
                        <FalseBranch>
                          <Action ActionType="1" Name="ASA1" Key="Condition9">
                            <ActionProperty Name="IfConnectionLogic" Value="1" />
                            <Checks>
                              <Check CheckType="2" Name="ASA5" Key="Check1" CheckNum="1">
                                <CheckProperty Name="IfCheckValueWhich" Value="1" />
                                <CheckProperty Name="IfCheckValueComponentID" Value="ASA" />
                                <CheckProperty Name="IfCheckValueRealComponentID" Value="ASA" />
                                <CheckProperty Name="IfCheckValueOperator" Value="1" />
                                <CheckProperty Name="IfCheckValueValue" Value="1$$C6$$" />
                              </Check>
                            </Checks>
                            <TrueBranch>
                              <Action ActionType="3" Name="ASA2" Key="Action15">
                                <ActionProperty Name="SetValueRealComponentID" Value="Choice1ASA" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Choice1ASA" />
                                <ActionProperty Name="SetValueComponentValue" Value="Healthy patient, no disease outside surgical process$$C6$$" />
                              </Action>
                            </TrueBranch>
                            <FalseBranch>
                              <Action ActionType="3" Name="ASA2" Key="Action16">
                                <ActionProperty Name="SetValueRealComponentID" Value="Choice1ASA" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Choice1ASA" />
                                <ActionProperty Name="SetValueComponentValue" Value="$$C6$$" />
                              </Action>
                            </FalseBranch>
                          </Action>
                        </FalseBranch>
                      </Action>
                    </FalseBranch>
                  </Action>
                </FalseBranch>
              </Action>
            </FalseBranch>
          </Action>
          <Action ActionType="3" Name="Choice8SurgeryQuick" Key="Action12">
            <ActionProperty Name="SetValueRealComponentID" Value="Choice8SurgeryQuick" />
            <ActionProperty Name="SetValueWhich" Value="1" />
            <ActionProperty Name="SetValueComponentID" Value="Choice8SurgeryQuick" />
            <ActionProperty Name="SetValueComponentValue" Value="Ortho$$C6$$" />
          </Action>
        </TrueBranch>
      </Action>
    </Script>
    <Script Name="CardiacRisk_ValueChanged" ProcType="3" CreationType="2" ParamCount="0" Component="">
      <Action ActionType="1" Name="Risk Interpretation (&gt;1%)" Key="Condition1">
        <ActionProperty Name="IfConnectionLogicType" Value="0" />
        <ActionProperty Name="IfConnectionLogic" Value="1" />
        <Checks>
          <Check CheckType="2" Name="Check1" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="CardiacRisk" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="CardiacRisk" />
            <CheckProperty Name="IfCheckValueOperator" Value="3" />
            <CheckProperty Name="IfCheckValueValue" Value="1$$C6$$" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="4" Name="High Risk" Key="Action4">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell21" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="Label17" />
          </Action>
          <Action ActionType="4" Name="Low Risk" Key="Action1">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell23" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="Label18" />
          </Action>
        </TrueBranch>
        <FalseBranch>
          <Action ActionType="1" Name="Condition2" Key="Condition2">
            <ActionProperty Name="IfConnectionLogicType" Value="0" />
            <ActionProperty Name="IfConnectionLogic" Value="1" />
            <Checks>
              <Check CheckType="2" Name="Check1" Key="Check1" CheckNum="1">
                <CheckProperty Name="IfCheckValueWhich" Value="1" />
                <CheckProperty Name="IfCheckValueComponentID" Value="CardiacRisk" />
                <CheckProperty Name="IfCheckValueRealComponentID" Value="CardiacRisk" />
                <CheckProperty Name="IfCheckValueOperator" Value="3" />
                <CheckProperty Name="IfCheckValueValue" Value="0$$C6$$" />
              </Check>
            </Checks>
            <TrueBranch>
              <Action ActionType="4" Name="Low Risk" Key="Action2">
                <ActionProperty Name="SetPropertyRealComponentID" Value="Cell23" />
                <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
                <ActionProperty Name="SetPropertyComponentID" Value="Label18" />
              </Action>
              <Action ActionType="4" Name="High Risk" Key="Action3">
                <ActionProperty Name="SetPropertyRealComponentID" Value="Cell21" />
                <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                <ActionProperty Name="SetPropertyComponentID" Value="Label17" />
              </Action>
            </TrueBranch>
            <FalseBranch>
              <Action ActionType="4" Name="Low Risk" Key="Action5">
                <ActionProperty Name="SetPropertyRealComponentID" Value="Cell23" />
                <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                <ActionProperty Name="SetPropertyComponentID" Value="Label18" />
              </Action>
              <Action ActionType="4" Name="High Risk" Key="Action6">
                <ActionProperty Name="SetPropertyRealComponentID" Value="Cell21" />
                <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                <ActionProperty Name="SetPropertyComponentID" Value="Label17" />
              </Action>
            </FalseBranch>
          </Action>
        </FalseBranch>
      </Action>
      <Action ActionType="1" Name="Percentile &gt; 7.69" Key="Condition3">
        <ActionProperty Name="IfConnectionLogicType" Value="0" />
        <ActionProperty Name="IfConnectionLogic" Value="1" />
        <Checks>
          <Check CheckType="2" Name="Greather than 7.69" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="CardiacRisk" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="CardiacRisk" />
            <CheckProperty Name="IfCheckValueOperator" Value="3" />
            <CheckProperty Name="IfCheckValueValue" Value="7.69$$C6$$" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="4" Name="97th" Key="Action8">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell8" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="Label14" />
          </Action>
          <Action ActionType="4" Name="96th-97th" Key="Action9">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell5" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="Label13" />
          </Action>
          <Action ActionType="4" Name="91st-95th" Key="Action10">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell18" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="Label15" />
          </Action>
          <Action ActionType="4" Name="51st-90th" Key="Action11">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell17" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="Label12" />
          </Action>
          <Action ActionType="4" Name="26th-50th" Key="Action12">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell3" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="Label11" />
          </Action>
          <Action ActionType="4" Name="&lt;25th" Key="Action7">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell1" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="Label10" />
          </Action>
        </TrueBranch>
        <FalseBranch>
          <Action ActionType="1" Name="&gt; 2.6" Key="Condition4">
            <ActionProperty Name="IfConnectionLogicType" Value="0" />
            <ActionProperty Name="IfConnectionLogic" Value="1" />
            <Checks>
              <Check CheckType="2" Name="Check1" Key="Check1" CheckNum="1">
                <CheckProperty Name="IfCheckValueWhich" Value="1" />
                <CheckProperty Name="IfCheckValueComponentID" Value="CardiacRisk" />
                <CheckProperty Name="IfCheckValueRealComponentID" Value="CardiacRisk" />
                <CheckProperty Name="IfCheckValueOperator" Value="3" />
                <CheckProperty Name="IfCheckValueValue" Value="2.60$$C6$$" />
              </Check>
            </Checks>
            <TrueBranch>
              <Action ActionType="4" Name="97th" Key="Action13">
                <ActionProperty Name="SetPropertyRealComponentID" Value="Cell8" />
                <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                <ActionProperty Name="SetPropertyComponentID" Value="Label14" />
              </Action>
              <Action ActionType="4" Name="96th-97th" Key="Action14">
                <ActionProperty Name="SetPropertyRealComponentID" Value="Cell5" />
                <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
                <ActionProperty Name="SetPropertyComponentID" Value="Label13" />
              </Action>
              <Action ActionType="4" Name="91st-95th" Key="Action15">
                <ActionProperty Name="SetPropertyRealComponentID" Value="Cell18" />
                <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                <ActionProperty Name="SetPropertyComponentID" Value="Label15" />
              </Action>
              <Action ActionType="4" Name="51st-90th" Key="Action16">
                <ActionProperty Name="SetPropertyRealComponentID" Value="Cell17" />
                <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                <ActionProperty Name="SetPropertyComponentID" Value="Label12" />
              </Action>
              <Action ActionType="4" Name="26th-50th" Key="Action17">
                <ActionProperty Name="SetPropertyRealComponentID" Value="Cell3" />
                <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                <ActionProperty Name="SetPropertyComponentID" Value="Label11" />
              </Action>
              <Action ActionType="4" Name="&lt;25th" Key="Action18">
                <ActionProperty Name="SetPropertyRealComponentID" Value="Cell1" />
                <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                <ActionProperty Name="SetPropertyComponentID" Value="Label10" />
              </Action>
            </TrueBranch>
            <FalseBranch>
              <Action ActionType="1" Name="&gt; 1.47" Key="Condition5">
                <ActionProperty Name="IfConnectionLogicType" Value="0" />
                <ActionProperty Name="IfConnectionLogic" Value="1" />
                <Checks>
                  <Check CheckType="2" Name="Check1" Key="Check1" CheckNum="1">
                    <CheckProperty Name="IfCheckValueWhich" Value="1" />
                    <CheckProperty Name="IfCheckValueComponentID" Value="CardiacRisk" />
                    <CheckProperty Name="IfCheckValueRealComponentID" Value="CardiacRisk" />
                    <CheckProperty Name="IfCheckValueOperator" Value="3" />
                    <CheckProperty Name="IfCheckValueValue" Value="1.47$$C6$$" />
                  </Check>
                </Checks>
                <TrueBranch>
                  <Action ActionType="4" Name="97th" Key="Action19">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="Cell8" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                    <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                    <ActionProperty Name="SetPropertyComponentID" Value="Label14" />
                  </Action>
                  <Action ActionType="4" Name="96th-97th" Key="Action20">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="Cell5" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                    <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                    <ActionProperty Name="SetPropertyComponentID" Value="Label13" />
                  </Action>
                  <Action ActionType="4" Name="91st-95th" Key="Action21">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="Cell18" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                    <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
                    <ActionProperty Name="SetPropertyComponentID" Value="Label15" />
                  </Action>
                  <Action ActionType="4" Name="51st-90th" Key="Action22">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="Cell17" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                    <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                    <ActionProperty Name="SetPropertyComponentID" Value="Label12" />
                  </Action>
                  <Action ActionType="4" Name="26th-50th" Key="Action23">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="Cell3" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                    <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                    <ActionProperty Name="SetPropertyComponentID" Value="Label11" />
                  </Action>
                  <Action ActionType="4" Name="&lt;25th" Key="Action24">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="Cell1" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                    <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                    <ActionProperty Name="SetPropertyComponentID" Value="Label10" />
                  </Action>
                </TrueBranch>
                <FalseBranch>
                  <Action ActionType="1" Name="&gt; 0.14" Key="Condition6">
                    <ActionProperty Name="IfConnectionLogicType" Value="0" />
                    <ActionProperty Name="IfConnectionLogic" Value="1" />
                    <Checks>
                      <Check CheckType="2" Name="Check1" Key="Check1" CheckNum="1">
                        <CheckProperty Name="IfCheckValueWhich" Value="1" />
                        <CheckProperty Name="IfCheckValueComponentID" Value="CardiacRisk" />
                        <CheckProperty Name="IfCheckValueRealComponentID" Value="CardiacRisk" />
                        <CheckProperty Name="IfCheckValueOperator" Value="3" />
                        <CheckProperty Name="IfCheckValueValue" Value="0.14$$C6$$" />
                      </Check>
                    </Checks>
                    <TrueBranch>
                      <Action ActionType="4" Name="97th" Key="Action25">
                        <ActionProperty Name="SetPropertyRealComponentID" Value="Cell8" />
                        <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                        <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                        <ActionProperty Name="SetPropertyComponentID" Value="Label14" />
                      </Action>
                      <Action ActionType="4" Name="96th-97th" Key="Action26">
                        <ActionProperty Name="SetPropertyRealComponentID" Value="Cell5" />
                        <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                        <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                        <ActionProperty Name="SetPropertyComponentID" Value="Label13" />
                      </Action>
                      <Action ActionType="4" Name="91st-95th" Key="Action27">
                        <ActionProperty Name="SetPropertyRealComponentID" Value="Cell18" />
                        <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                        <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                        <ActionProperty Name="SetPropertyComponentID" Value="Label15" />
                      </Action>
                      <Action ActionType="4" Name="51st-90th" Key="Action28">
                        <ActionProperty Name="SetPropertyRealComponentID" Value="Cell17" />
                        <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                        <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
                        <ActionProperty Name="SetPropertyComponentID" Value="Label12" />
                      </Action>
                      <Action ActionType="4" Name="26th-50th" Key="Action29">
                        <ActionProperty Name="SetPropertyRealComponentID" Value="Cell3" />
                        <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                        <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                        <ActionProperty Name="SetPropertyComponentID" Value="Label11" />
                      </Action>
                      <Action ActionType="4" Name="&lt;25th" Key="Action30">
                        <ActionProperty Name="SetPropertyRealComponentID" Value="Cell1" />
                        <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                        <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                        <ActionProperty Name="SetPropertyComponentID" Value="Label10" />
                      </Action>
                    </TrueBranch>
                    <FalseBranch>
                      <Action ActionType="1" Name="&gt; 0.05" Key="Condition7">
                        <ActionProperty Name="IfConnectionLogicType" Value="0" />
                        <ActionProperty Name="IfConnectionLogic" Value="1" />
                        <Checks>
                          <Check CheckType="2" Name="Check1" Key="Check1" CheckNum="1">
                            <CheckProperty Name="IfCheckValueWhich" Value="1" />
                            <CheckProperty Name="IfCheckValueComponentID" Value="CardiacRisk" />
                            <CheckProperty Name="IfCheckValueRealComponentID" Value="CardiacRisk" />
                            <CheckProperty Name="IfCheckValueOperator" Value="3" />
                            <CheckProperty Name="IfCheckValueValue" Value="0.05$$C6$$" />
                          </Check>
                        </Checks>
                        <TrueBranch>
                          <Action ActionType="4" Name="97th" Key="Action31">
                            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell8" />
                            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                            <ActionProperty Name="SetPropertyComponentID" Value="Label14" />
                          </Action>
                          <Action ActionType="4" Name="96th-97th" Key="Action32">
                            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell5" />
                            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                            <ActionProperty Name="SetPropertyComponentID" Value="Label13" />
                          </Action>
                          <Action ActionType="4" Name="91st-95th" Key="Action33">
                            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell18" />
                            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                            <ActionProperty Name="SetPropertyComponentID" Value="Label15" />
                          </Action>
                          <Action ActionType="4" Name="51st-90th" Key="Action34">
                            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell17" />
                            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                            <ActionProperty Name="SetPropertyComponentID" Value="Label12" />
                          </Action>
                          <Action ActionType="4" Name="26th-50th" Key="Action35">
                            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell3" />
                            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
                            <ActionProperty Name="SetPropertyComponentID" Value="Label11" />
                          </Action>
                          <Action ActionType="4" Name="&lt;26th" Key="Action36">
                            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell1" />
                            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                            <ActionProperty Name="SetPropertyComponentID" Value="Label10" />
                          </Action>
                        </TrueBranch>
                        <FalseBranch>
                          <Action ActionType="1" Name="Not Zero" Key="Condition8">
                            <ActionProperty Name="IfConnectionLogicType" Value="0" />
                            <ActionProperty Name="IfConnectionLogic" Value="1" />
                            <Checks>
                              <Check CheckType="2" Name="Check1" Key="Check1" CheckNum="1">
                                <CheckProperty Name="IfCheckValueWhich" Value="1" />
                                <CheckProperty Name="IfCheckValueComponentID" Value="CardiacRisk" />
                                <CheckProperty Name="IfCheckValueRealComponentID" Value="CardiacRisk" />
                                <CheckProperty Name="IfCheckValueOperator" Value="3" />
                                <CheckProperty Name="IfCheckValueValue" Value="0$$C6$$" />
                              </Check>
                            </Checks>
                            <TrueBranch>
                              <Action ActionType="4" Name="97th" Key="Action37">
                                <ActionProperty Name="SetPropertyRealComponentID" Value="Cell8" />
                                <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                                <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                                <ActionProperty Name="SetPropertyComponentID" Value="Label14" />
                              </Action>
                              <Action ActionType="4" Name="96th-97th" Key="Action38">
                                <ActionProperty Name="SetPropertyRealComponentID" Value="Cell5" />
                                <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                                <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                                <ActionProperty Name="SetPropertyComponentID" Value="Label13" />
                              </Action>
                              <Action ActionType="4" Name="91st-95th" Key="Action39">
                                <ActionProperty Name="SetPropertyRealComponentID" Value="Cell18" />
                                <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                                <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                                <ActionProperty Name="SetPropertyComponentID" Value="Label15" />
                              </Action>
                              <Action ActionType="4" Name="51st-90th" Key="Action40">
                                <ActionProperty Name="SetPropertyRealComponentID" Value="Cell17" />
                                <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                                <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                                <ActionProperty Name="SetPropertyComponentID" Value="Label12" />
                              </Action>
                              <Action ActionType="4" Name="26th-50th" Key="Action41">
                                <ActionProperty Name="SetPropertyRealComponentID" Value="Cell3" />
                                <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                                <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                                <ActionProperty Name="SetPropertyComponentID" Value="Label11" />
                              </Action>
                              <Action ActionType="4" Name="&lt;25th" Key="Action42">
                                <ActionProperty Name="SetPropertyRealComponentID" Value="Cell1" />
                                <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                                <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
                                <ActionProperty Name="SetPropertyComponentID" Value="Label10" />
                              </Action>
                            </TrueBranch>
                            <FalseBranch>
                              <Action ActionType="4" Name="97th" Key="Action49">
                                <ActionProperty Name="SetPropertyRealComponentID" Value="Cell8" />
                                <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                                <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                                <ActionProperty Name="SetPropertyComponentID" Value="Label14" />
                              </Action>
                              <Action ActionType="4" Name="51st-90th" Key="Action52">
                                <ActionProperty Name="SetPropertyRealComponentID" Value="Cell17" />
                                <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                                <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                                <ActionProperty Name="SetPropertyComponentID" Value="Label12" />
                              </Action>
                              <Action ActionType="4" Name="&lt;25th" Key="Action54">
                                <ActionProperty Name="SetPropertyRealComponentID" Value="Cell1" />
                                <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                                <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                                <ActionProperty Name="SetPropertyComponentID" Value="Label10" />
                              </Action>
                              <Action ActionType="4" Name="96th-97th" Key="Action50">
                                <ActionProperty Name="SetPropertyRealComponentID" Value="Cell5" />
                                <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                                <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                                <ActionProperty Name="SetPropertyComponentID" Value="Label13" />
                              </Action>
                              <Action ActionType="4" Name="26th-50th" Key="Action53">
                                <ActionProperty Name="SetPropertyRealComponentID" Value="Cell3" />
                                <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                                <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                                <ActionProperty Name="SetPropertyComponentID" Value="Label11" />
                              </Action>
                              <Action ActionType="4" Name="91st-95th" Key="Action51">
                                <ActionProperty Name="SetPropertyRealComponentID" Value="Cell18" />
                                <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                                <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                                <ActionProperty Name="SetPropertyComponentID" Value="Label15" />
                              </Action>
                            </FalseBranch>
                          </Action>
                        </FalseBranch>
                      </Action>
                    </FalseBranch>
                  </Action>
                </FalseBranch>
              </Action>
            </FalseBranch>
          </Action>
        </FalseBranch>
      </Action>
    </Script>
    <Script Name="ASA_ValueChanged" ProcType="3" CreationType="2" ParamCount="0" Component="">
      <Action ActionType="1" Name="Choice1ASA" Key="Condition1">
        <ActionProperty Name="IfConnectionLogic" Value="1" />
        <Checks>
          <Check CheckType="2" Name="ASA5" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="ASA" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="ASA" />
            <CheckProperty Name="IfCheckValueOperator" Value="1" />
            <CheckProperty Name="IfCheckValueValue" Value="5$$C6$$" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="3" Name="ASA5" Key="Action1">
            <ActionProperty Name="SetValueRealComponentID" Value="Choice1ASA" />
            <ActionProperty Name="SetValueWhich" Value="1" />
            <ActionProperty Name="SetValueComponentID" Value="Choice1ASA" />
            <ActionProperty Name="SetValueComponentValue" Value="Moribund patient not expected to survive 24 hours without an operation$$C6$$" />
          </Action>
        </TrueBranch>
        <FalseBranch>
          <Action ActionType="1" Name="ASA4" Key="Condition2">
            <ActionProperty Name="IfConnectionLogic" Value="1" />
            <Checks>
              <Check CheckType="2" Name="ASA5" Key="Check1" CheckNum="1">
                <CheckProperty Name="IfCheckValueWhich" Value="1" />
                <CheckProperty Name="IfCheckValueComponentID" Value="ASA" />
                <CheckProperty Name="IfCheckValueRealComponentID" Value="ASA" />
                <CheckProperty Name="IfCheckValueOperator" Value="1" />
                <CheckProperty Name="IfCheckValueValue" Value="4$$C6$$" />
              </Check>
            </Checks>
            <TrueBranch>
              <Action ActionType="3" Name="ASA4" Key="Action2">
                <ActionProperty Name="SetValueRealComponentID" Value="Choice1ASA" />
                <ActionProperty Name="SetValueWhich" Value="1" />
                <ActionProperty Name="SetValueComponentID" Value="Choice1ASA" />
                <ActionProperty Name="SetValueComponentValue" Value="Severe incapacitating disease process that is a constant threat to life$$C6$$" />
              </Action>
            </TrueBranch>
            <FalseBranch>
              <Action ActionType="1" Name="ASA3" Key="Condition3">
                <ActionProperty Name="IfConnectionLogic" Value="1" />
                <Checks>
                  <Check CheckType="2" Name="ASA5" Key="Check1" CheckNum="1">
                    <CheckProperty Name="IfCheckValueWhich" Value="1" />
                    <CheckProperty Name="IfCheckValueComponentID" Value="ASA" />
                    <CheckProperty Name="IfCheckValueRealComponentID" Value="ASA" />
                    <CheckProperty Name="IfCheckValueOperator" Value="1" />
                    <CheckProperty Name="IfCheckValueValue" Value="3$$C6$$" />
                  </Check>
                </Checks>
                <TrueBranch>
                  <Action ActionType="3" Name="ASA3" Key="Action3">
                    <ActionProperty Name="SetValueRealComponentID" Value="Choice1ASA" />
                    <ActionProperty Name="SetValueWhich" Value="1" />
                    <ActionProperty Name="SetValueComponentID" Value="Choice1ASA" />
                    <ActionProperty Name="SetValueComponentValue" Value="Severe systemic disease that results in functional limitation$$C6$$" />
                  </Action>
                </TrueBranch>
                <FalseBranch>
                  <Action ActionType="1" Name="ASA2" Key="Condition4">
                    <ActionProperty Name="IfConnectionLogic" Value="1" />
                    <Checks>
                      <Check CheckType="2" Name="ASA5" Key="Check1" CheckNum="1">
                        <CheckProperty Name="IfCheckValueWhich" Value="1" />
                        <CheckProperty Name="IfCheckValueComponentID" Value="ASA" />
                        <CheckProperty Name="IfCheckValueRealComponentID" Value="ASA" />
                        <CheckProperty Name="IfCheckValueOperator" Value="1" />
                        <CheckProperty Name="IfCheckValueValue" Value="2$$C6$$" />
                      </Check>
                    </Checks>
                    <TrueBranch>
                      <Action ActionType="3" Name="ASA2" Key="Action4">
                        <ActionProperty Name="SetValueRealComponentID" Value="Choice1ASA" />
                        <ActionProperty Name="SetValueWhich" Value="1" />
                        <ActionProperty Name="SetValueComponentID" Value="Choice1ASA" />
                        <ActionProperty Name="SetValueComponentValue" Value="Mild to moderate systemic disease, medically well controlled, with no functional limitation$$C6$$" />
                      </Action>
                    </TrueBranch>
                    <FalseBranch>
                      <Action ActionType="1" Name="ASA1" Key="Condition5">
                        <ActionProperty Name="IfConnectionLogic" Value="1" />
                        <Checks>
                          <Check CheckType="2" Name="ASA5" Key="Check1" CheckNum="1">
                            <CheckProperty Name="IfCheckValueWhich" Value="1" />
                            <CheckProperty Name="IfCheckValueComponentID" Value="ASA" />
                            <CheckProperty Name="IfCheckValueRealComponentID" Value="ASA" />
                            <CheckProperty Name="IfCheckValueOperator" Value="1" />
                            <CheckProperty Name="IfCheckValueValue" Value="1$$C6$$" />
                          </Check>
                        </Checks>
                        <TrueBranch>
                          <Action ActionType="3" Name="ASA2" Key="Action5">
                            <ActionProperty Name="SetValueRealComponentID" Value="Choice1ASA" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="Choice1ASA" />
                            <ActionProperty Name="SetValueComponentValue" Value="Healthy patient, no disease outside surgical process$$C6$$" />
                          </Action>
                        </TrueBranch>
                        <FalseBranch>
                          <Action ActionType="3" Name="ASA2" Key="Action6">
                            <ActionProperty Name="SetValueRealComponentID" Value="Choice1ASA" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="Choice1ASA" />
                            <ActionProperty Name="SetValueComponentValue" Value="$$C6$$" />
                          </Action>
                        </FalseBranch>
                      </Action>
                    </FalseBranch>
                  </Action>
                </FalseBranch>
              </Action>
            </FalseBranch>
          </Action>
        </FalseBranch>
      </Action>
    </Script>
  </FormScripts>
</Form>
```
