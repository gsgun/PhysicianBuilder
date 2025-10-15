---
description: >-
  Honestly, this thing is awful. Please look at PCI GDMT Smartform for better
  logic build. Moving this PKG takes minutes
---

# XML

```
Gradio Text Gen:

<?xml version="1.0" encoding="Windows-1252"?>
<?FormVersion 6.0?>
<?FormSize 154:26?>
<Form>
  <Cmpnt Type="EACSFComponents*.ACSFForm" Name="ARootComponent">
    <Prps>
      <Prp Name="Back color">#FFFFFF</Prp>
      <Prp Name="Title text">Predicting Risk of CVD Events</Prp>
      <Prp Name="Flowsheet template">640
PH T CVDR
640</Prp>
      <Prp Name="Title style">2</Prp>
      <Prp Name="Wrap captions">True</Prp>
      <Prp Name="Show title button">False</Prp>
      <Prp Name="Width">71%</Prp>
      <Prp Name="Title font">;;;;False;False;</Prp>
      <Prp Name="Use theming">1</Prp>
    </Prps>
    <Chld>
      <Cmpnt Type="EACSFComponents*.ACSFTableRow" Name="Row1">
        <Prps>
          <Prp Name="Rows">1</Prp>
          <Prp Name="Columns">1</Prp>
        </Prps>
        <Chld>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell1" DSrc="3" DFld="1" DCnt="1" DTyp="6">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Prompt width">125px</Prp>
              <Prp Name="Back color">#FFFFFF</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">5px</Prp>
              <Prp Name="Padding">5px</Prp>
              <Prp Name="Width">45%</Prp>
              <Prp Name="Cell row">1</Prp>
              <Prp Name="Prompt">History of ASCVD</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFList" Name="HxofASCVD" DSrc="3" DFld="2" DCnt="1" DTyp="6">
                <Prps>
                  <Prp Name="ListSource">3</Prp>
                  <Prp Name="Choices">Yes;No</Prp>
                  <Prp Name="ListCUI">15832</Prp>
                  <Prp Name="Multiple select">False</Prp>
                  <Prp Name="Tooltip text">Yes=1;No=0</Prp>
                  <Prp Name="Wrap options">False</Prp>
                  <Prp Name="Sizing">1</Prp>
                </Prps>
              </Cmpnt>
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
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell2" DSrc="3" DFld="3" DCnt="1" DTyp="6">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Prompt width">125px</Prp>
              <Prp Name="Back color">#FFFFFF</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">5px</Prp>
              <Prp Name="Padding">5px</Prp>
              <Prp Name="Height">37px</Prp>
              <Prp Name="Width">71%</Prp>
              <Prp Name="Cell row">1</Prp>
              <Prp Name="Prompt">Sex</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFList" Name="Sex" DSrc="3" DFld="4" DCnt="1" DTyp="6">
                <Prps>
                  <Prp Name="ListSource">3</Prp>
                  <Prp Name="Choices">Male;Female;X</Prp>
                  <Prp Name="ListCUI">15815</Prp>
                  <Prp Name="Multiple select">False</Prp>
                  <Prp Name="Tooltip text">Male=2;Female=1;X=3</Prp>
                  <Prp Name="Wrap options">False</Prp>
                  <Prp Name="Sizing">1</Prp>
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
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell3" DSrc="3" DFld="5" DCnt="1" DTyp="6">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Prompt width">125px</Prp>
              <Prp Name="Back color">#FFFFFF</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">5px</Prp>
              <Prp Name="Padding">5px</Prp>
              <Prp Name="Height">22px</Prp>
              <Prp Name="Width">45%</Prp>
              <Prp Name="Cell row">1</Prp>
              <Prp Name="Prompt">Diabetes</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFList" Name="Diabetes" DSrc="3" DFld="6" DCnt="1" DTyp="6">
                <Prps>
                  <Prp Name="ListSource">3</Prp>
                  <Prp Name="Choices">Yes;No</Prp>
                  <Prp Name="ListCUI">15816</Prp>
                  <Prp Name="Multiple select">False</Prp>
                  <Prp Name="Tooltip text">Yes=1;No=0</Prp>
                  <Prp Name="Wrap options">False</Prp>
                  <Prp Name="Sizing">1</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
        </Chld>
      </Cmpnt>
      <Cmpnt Type="EACSFComponents*.ACSFTableRow" Name="Row4">
        <Prps>
          <Prp Name="Rows">1</Prp>
          <Prp Name="Columns">5</Prp>
        </Prps>
        <Chld>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell4" DSrc="3" DFld="7" DCnt="1" DTyp="6">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Prompt width">125px</Prp>
              <Prp Name="Back color">#FFFFFF</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">5px</Prp>
              <Prp Name="Padding">5px</Prp>
              <Prp Name="Height">22px</Prp>
              <Prp Name="Width">45%</Prp>
              <Prp Name="Cell row">1</Prp>
              <Prp Name="Prompt">Current Smoker</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFList" Name="Smoker" DSrc="3" DFld="8" DCnt="1" DTyp="6">
                <Prps>
                  <Prp Name="ListSource">3</Prp>
                  <Prp Name="Choices">Yes;No</Prp>
                  <Prp Name="ListCUI">15841</Prp>
                  <Prp Name="Multiple select">False</Prp>
                  <Prp Name="Tooltip text">Yes=1;No=0</Prp>
                  <Prp Name="Wrap options">False</Prp>
                  <Prp Name="Sizing">1</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell100">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Visible">False</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Height">36px</Prp>
              <Prp Name="Width">18%</Prp>
              <Prp Name="Cell row">1</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFLabel" Name="Risk3">
                <Prps>
                  <Prp Name="Tooltip text">CVD Risk</Prp>
                  <Prp Name="Caption">Intermediate risk (7.5% to 19.9%)</Prp>
                  <Prp Name="Label type">7</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell102">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Visible">False</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Height">22px</Prp>
              <Prp Name="Width">11%</Prp>
              <Prp Name="Cell row">1</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFLabel" Name="Risk4">
                <Prps>
                  <Prp Name="Tooltip text">CVD Risk</Prp>
                  <Prp Name="Caption">High risk (&gt;20%)</Prp>
                  <Prp Name="Label type">8</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell98">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Visible">False</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Height">22px</Prp>
              <Prp Name="Width">13%</Prp>
              <Prp Name="Cell row">1</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFLabel" Name="Risk2">
                <Prps>
                  <Prp Name="Tooltip text">CVD Risk</Prp>
                  <Prp Name="Caption">Borderline risk (5% to 7.4%)</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell94">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Visible">False</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Height">22px</Prp>
              <Prp Name="Width">18%</Prp>
              <Prp Name="Cell row">1</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFLabel" Name="Risk0">
                <Prps>
                  <Prp Name="Tooltip text">CVD Risk</Prp>
                  <Prp Name="Caption">Low risk (&lt;5%)</Prp>
                  <Prp Name="Label type">5</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
        </Chld>
      </Cmpnt>
      <Cmpnt Type="EACSFComponents*.ACSFTableRow" Name="Row10">
        <Prps>
          <Prp Name="Rows">4</Prp>
          <Prp Name="Columns">9</Prp>
        </Prps>
        <Chld>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell9" DSrc="3" DFld="9" DCnt="1" DTyp="2">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Prompt width">125px</Prp>
              <Prp Name="Back color">#FFFFFF</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">10px</Prp>
              <Prp Name="Height">27px</Prp>
              <Prp Name="Width">17%</Prp>
              <Prp Name="Cell row">1</Prp>
              <Prp Name="Prompt">10 yr ASCVD</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFChrontrol" Name="ASCVD10" DSrc="3" DFld="10" DCnt="1" DTyp="2">
                <Prps>
                  <Prp Name="Tooltip text">Coronary + Stroke Risk</Prp>
                  <Prp Name="Enabled">False</Prp>
                  <Prp Name="Requirements">1</Prp>
                  <Prp Name="Field properties">EACSFControls*.ACSFChrontrolPPG</Prp>
                  <Prp Name="Allow negative values">0</Prp>
                  <Prp Name="PropertyPageData">N~1#######~Y~####12##########~G~16777215###~	~##~</Prp>
                  <Prp Name="PPG Has Entry Button Set">True</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell107">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Height">29px</Prp>
              <Prp Name="Width">8%</Prp>
              <Prp Name="Cell row">1</Prp>
              <Prp Name="Prompt">%</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFSpacer" Name="Spacer65" />
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell7" DSrc="3" DFld="11" DCnt="1" DTyp="2">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Prompt width">125px</Prp>
              <Prp Name="Back color">#FFFFFF</Prp>
              <Prp Name="Component indent">0px</Prp>
              <Prp Name="Prompt indent">0px</Prp>
              <Prp Name="Height">27px</Prp>
              <Prp Name="Width">3%</Prp>
              <Prp Name="Cell row">1</Prp>
              <Prp Name="Prompt">10 yr CVD</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFChrontrol" Name="CVD10" DSrc="3" DFld="12" DCnt="1" DTyp="2">
                <Prps>
                  <Prp Name="Tooltip text">Coronary + Stroke + Heart Failure Risk</Prp>
                  <Prp Name="Enabled">False</Prp>
                  <Prp Name="Requirements">1</Prp>
                  <Prp Name="Field properties">EACSFControls*.ACSFChrontrolPPG</Prp>
                  <Prp Name="Allow negative values">0</Prp>
                  <Prp Name="PropertyPageData">N~1#######~Y~####12##########~G~16777215###~	~##~</Prp>
                  <Prp Name="PPG Has Entry Button Set">True</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell59">
            <Prps>
              <Prp Name="Column span">2</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Height">26px</Prp>
              <Prp Name="Width">15%</Prp>
              <Prp Name="Cell row">1</Prp>
              <Prp Name="Prompt">%</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFSpacer" Name="Spacer26" />
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell88">
            <Prps>
              <Prp Name="Column span">4</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Width">92%</Prp>
              <Prp Name="Cell row">1</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFSpacer" Name="Spacer48" />
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell40" DSrc="3" DFld="13" DCnt="1" DTyp="2">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Prompt width">125px</Prp>
              <Prp Name="Back color">#FFFFFF</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">10px</Prp>
              <Prp Name="Height">29px</Prp>
              <Prp Name="Width">17%</Prp>
              <Prp Name="Cell row">2</Prp>
              <Prp Name="Prompt">10 yr Coronary</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFChrontrol" Name="CHD10" DSrc="3" DFld="14" DCnt="1" DTyp="2">
                <Prps>
                  <Prp Name="Enabled">False</Prp>
                  <Prp Name="Requirements">1</Prp>
                  <Prp Name="Field properties">EACSFControls*.ACSFChrontrolPPG</Prp>
                  <Prp Name="Allow negative values">0</Prp>
                  <Prp Name="PropertyPageData">N~1#######~Y~####12##########~G~16777215###~	~##~</Prp>
                  <Prp Name="PPG Has Entry Button Set">True</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell57">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Height">26px</Prp>
              <Prp Name="Width">8%</Prp>
              <Prp Name="Cell row">2</Prp>
              <Prp Name="Prompt">%</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFSpacer" Name="Spacer24" />
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell16" DSrc="3" DFld="15" DCnt="1" DTyp="2">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Prompt width">125px</Prp>
              <Prp Name="Component indent">0px</Prp>
              <Prp Name="Prompt indent">0px</Prp>
              <Prp Name="Height">30px</Prp>
              <Prp Name="Width">3%</Prp>
              <Prp Name="Cell row">2</Prp>
              <Prp Name="Prompt">10 yr Stroke</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFChrontrol" Name="CVA10" DSrc="3" DFld="16" DCnt="1" DTyp="2">
                <Prps>
                  <Prp Name="Enabled">False</Prp>
                  <Prp Name="Requirements">1</Prp>
                  <Prp Name="Field properties">EACSFControls*.ACSFChrontrolPPG</Prp>
                  <Prp Name="Allow negative values">0</Prp>
                  <Prp Name="PropertyPageData">N~1#######~Y~####12##########~G~16777215###~	~##~</Prp>
                  <Prp Name="PPG Has Entry Button Set">True</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell61">
            <Prps>
              <Prp Name="Column span">2</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Height">26px</Prp>
              <Prp Name="Width">5%</Prp>
              <Prp Name="Cell row">2</Prp>
              <Prp Name="Prompt">%</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFSpacer" Name="Spacer28" />
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell67" DSrc="3" DFld="17" DCnt="1" DTyp="2">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Prompt width">125px</Prp>
              <Prp Name="Back color">#FFFFFF</Prp>
              <Prp Name="Component indent">0px</Prp>
              <Prp Name="Prompt indent">0px</Prp>
              <Prp Name="Height">27px</Prp>
              <Prp Name="Width">7.5%</Prp>
              <Prp Name="Cell row">2</Prp>
              <Prp Name="Prompt">10 yr Heart Failure</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFChrontrol" Name="HF10" DSrc="3" DFld="18" DCnt="1" DTyp="2">
                <Prps>
                  <Prp Name="Enabled">False</Prp>
                  <Prp Name="Requirements">1</Prp>
                  <Prp Name="Field properties">EACSFControls*.ACSFChrontrolPPG</Prp>
                  <Prp Name="Allow negative values">0</Prp>
                  <Prp Name="PropertyPageData">N~1#######~Y~####12##########~G~16777215#0##~	~##~</Prp>
                  <Prp Name="PPG Has Entry Button Set">False</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell14">
            <Prps>
              <Prp Name="Column span">3</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Height">32px</Prp>
              <Prp Name="Width">4%</Prp>
              <Prp Name="Cell row">2</Prp>
              <Prp Name="Prompt">%</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFSpacer" Name="Spacer11" />
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell41" DSrc="3" DFld="19" DCnt="1" DTyp="0">
            <Prps>
              <Prp Name="Column span">9</Prp>
              <Prp Name="Border">0,1px,#000000;0,1px,#000000;0,1px,#000000;3,1px,#000000</Prp>
              <Prp Name="Prompt width">125px</Prp>
              <Prp Name="Separate binding">True</Prp>
              <Prp Name="Back color">#FFFFFF</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">5px</Prp>
              <Prp Name="Padding">5px</Prp>
              <Prp Name="Height">33px</Prp>
              <Prp Name="Width">17%</Prp>
              <Prp Name="Cell row">3</Prp>
              <Prp Name="Prompt">Values</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFChrontrol" Name="VariableNotHF" DSrc="3" DFld="20" DCnt="1" DTyp="0">
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
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell75" DSrc="3" DFld="21" DCnt="1" DTyp="0">
            <Prps>
              <Prp Name="Column span">9</Prp>
              <Prp Name="Prompt width">125px</Prp>
              <Prp Name="Visible">False</Prp>
              <Prp Name="Back color">#FFFFFF</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">5px</Prp>
              <Prp Name="Padding">5px</Prp>
              <Prp Name="Height">26px</Prp>
              <Prp Name="Width">17%</Prp>
              <Prp Name="Cell row">4</Prp>
              <Prp Name="Prompt">Heart Failure Values</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFChrontrol" Name="VariableHF" DSrc="3" DFld="22" DCnt="1" DTyp="0">
                <Prps>
                  <Prp Name="Enabled">False</Prp>
                  <Prp Name="Requirements">1</Prp>
                  <Prp Name="Field properties">EACSFControls*.ACSFChrontrolPPG</Prp>
                  <Prp Name="Allow negative values">0</Prp>
                  <Prp Name="PropertyPageData">A~###~Y~####16##########~G~16777215#0##~	~##~</Prp>
                  <Prp Name="PPG Has Entry Button Set">False</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
        </Chld>
      </Cmpnt>
      <Cmpnt Type="EACSFComponents*.ACSFTableRow" Name="Row9">
        <Prps>
          <Prp Name="Rows">8</Prp>
          <Prp Name="Columns">9</Prp>
        </Prps>
        <Chld>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell99">
            <Prps>
              <Prp Name="Column span">9</Prp>
              <Prp Name="Prompt width">125px</Prp>
              <Prp Name="Visible">False</Prp>
              <Prp Name="Component indent">5px</Prp>
              <Prp Name="Prompt indent">10px</Prp>
              <Prp Name="Height">22px</Prp>
              <Prp Name="Width">15%</Prp>
              <Prp Name="Cell row">1</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFLabel" Name="SimTitle">
                <Prps>
                  <Prp Name="Font">Arial;16pt;bold;normal;false;false;#000000</Prp>
                  <Prp Name="Caption">Simulation Activity</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell19" DSrc="3" DFld="23" DCnt="1" DTyp="2">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Prompt width">125px</Prp>
              <Prp Name="Visible">False</Prp>
              <Prp Name="Back color">#FFFFFF</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">10px</Prp>
              <Prp Name="Height">27px</Prp>
              <Prp Name="Width">23%</Prp>
              <Prp Name="Cell row">2</Prp>
              <Prp Name="Prompt">10 yr ASCVD Sim</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFChrontrol" Name="SimASCVd" DSrc="3" DFld="24" DCnt="1" DTyp="2">
                <Prps>
                  <Prp Name="Enabled">False</Prp>
                  <Prp Name="Requirements">1</Prp>
                  <Prp Name="Field properties">EACSFControls*.ACSFChrontrolPPG</Prp>
                  <Prp Name="Allow negative values">0</Prp>
                  <Prp Name="PropertyPageData">N~1#######~Y~####12##########~G~16777215###~	~##~</Prp>
                  <Prp Name="PPG Has Entry Button Set">True</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="per1">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Visible">False</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Height">29px</Prp>
              <Prp Name="Width">2%</Prp>
              <Prp Name="Cell row">2</Prp>
              <Prp Name="Prompt">%</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFSpacer" Name="Spacer225" />
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell20" DSrc="3" DFld="25" DCnt="1" DTyp="2">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Prompt width">125px</Prp>
              <Prp Name="Visible">False</Prp>
              <Prp Name="Back color">#FFFFFF</Prp>
              <Prp Name="Component indent">0px</Prp>
              <Prp Name="Prompt indent">0px</Prp>
              <Prp Name="Height">26px</Prp>
              <Prp Name="Width">5%</Prp>
              <Prp Name="Cell row">2</Prp>
              <Prp Name="Prompt">10 yr CVD Sim</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFChrontrol" Name="SimCVD" DSrc="3" DFld="26" DCnt="1" DTyp="2">
                <Prps>
                  <Prp Name="Enabled">False</Prp>
                  <Prp Name="Requirements">1</Prp>
                  <Prp Name="Field properties">EACSFControls*.ACSFChrontrolPPG</Prp>
                  <Prp Name="Allow negative values">0</Prp>
                  <Prp Name="PropertyPageData">N~1#######~Y~####12##########~G~16777215###~	~##~</Prp>
                  <Prp Name="PPG Has Entry Button Set">True</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="per3">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Visible">False</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Height">26px</Prp>
              <Prp Name="Width">10%</Prp>
              <Prp Name="Cell row">2</Prp>
              <Prp Name="Prompt">%</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFSpacer" Name="Spacer74" />
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell24">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Visible">False</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Height">26px</Prp>
              <Prp Name="Width">14%</Prp>
              <Prp Name="Cell row">2</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFSpacer" Name="Spacer3" />
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell15">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Visible">False</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Height">26px</Prp>
              <Prp Name="Width">14%</Prp>
              <Prp Name="Cell row">2</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFSpacer" Name="Spacer2" />
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell77">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Visible">False</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Height">26px</Prp>
              <Prp Name="Width">8%</Prp>
              <Prp Name="Cell row">2</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFLabel" Name="SignCVD">
                <Prps>
                  <Prp Name="Caption">SignCVD</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell72">
            <Prps>
              <Prp Name="Column span">2</Prp>
              <Prp Name="Visible">False</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Height">26px</Prp>
              <Prp Name="Width">27%</Prp>
              <Prp Name="Cell row">2</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFLabel" Name="DifCVD">
                <Prps>
                  <Prp Name="Caption">CVDDif</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell26" DSrc="3" DFld="27" DCnt="1" DTyp="2">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Prompt width">125px</Prp>
              <Prp Name="Visible">False</Prp>
              <Prp Name="Back color">#FFFFFF</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">10px</Prp>
              <Prp Name="Height">32px</Prp>
              <Prp Name="Width">26%</Prp>
              <Prp Name="Cell row">3</Prp>
              <Prp Name="Prompt">10 yr Coronary Sim</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFChrontrol" Name="SimCHD" DSrc="3" DFld="28" DCnt="1" DTyp="2">
                <Prps>
                  <Prp Name="Enabled">False</Prp>
                  <Prp Name="Requirements">1</Prp>
                  <Prp Name="Field properties">EACSFControls*.ACSFChrontrolPPG</Prp>
                  <Prp Name="Allow negative values">0</Prp>
                  <Prp Name="PropertyPageData">N~1#######~Y~####12##########~G~16777215###~	~##~</Prp>
                  <Prp Name="PPG Has Entry Button Set">True</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="per2">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Visible">False</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Height">32px</Prp>
              <Prp Name="Width">2%</Prp>
              <Prp Name="Cell row">3</Prp>
              <Prp Name="Prompt">%</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFSpacer" Name="Spacer226" />
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell27" DSrc="3" DFld="29" DCnt="1" DTyp="2">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Prompt width">125px</Prp>
              <Prp Name="Visible">False</Prp>
              <Prp Name="Back color">#FFFFFF</Prp>
              <Prp Name="Component indent">0px</Prp>
              <Prp Name="Prompt indent">0px</Prp>
              <Prp Name="Height">32px</Prp>
              <Prp Name="Width">3%</Prp>
              <Prp Name="Cell row">3</Prp>
              <Prp Name="Prompt">10 yr Stroke Sim</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFChrontrol" Name="SimCVA" DSrc="3" DFld="30" DCnt="1" DTyp="2">
                <Prps>
                  <Prp Name="Enabled">False</Prp>
                  <Prp Name="Requirements">1</Prp>
                  <Prp Name="Field properties">EACSFControls*.ACSFChrontrolPPG</Prp>
                  <Prp Name="Allow negative values">0</Prp>
                  <Prp Name="PropertyPageData">N~1#######~Y~####12##########~G~16777215###~	~##~</Prp>
                  <Prp Name="PPG Has Entry Button Set">True</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="per4">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Visible">False</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Height">32px</Prp>
              <Prp Name="Width">10%</Prp>
              <Prp Name="Cell row">3</Prp>
              <Prp Name="Prompt">%</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFSpacer" Name="Spacer89" />
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell28" DSrc="3" DFld="31" DCnt="1" DTyp="2">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Prompt width">125px</Prp>
              <Prp Name="Visible">False</Prp>
              <Prp Name="Back color">#FFFFFF</Prp>
              <Prp Name="Component indent">0px</Prp>
              <Prp Name="Prompt indent">0px</Prp>
              <Prp Name="Height">32px</Prp>
              <Prp Name="Width">42%</Prp>
              <Prp Name="Cell row">3</Prp>
              <Prp Name="Prompt">10 yr Heart Failure Sim</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFChrontrol" Name="SimHF" DSrc="3" DFld="32" DCnt="1" DTyp="2">
                <Prps>
                  <Prp Name="Enabled">False</Prp>
                  <Prp Name="Requirements">1</Prp>
                  <Prp Name="Field properties">EACSFControls*.ACSFChrontrolPPG</Prp>
                  <Prp Name="Allow negative values">0</Prp>
                  <Prp Name="PropertyPageData">N~1#######~Y~####12##########~G~16777215#0##~	~##~</Prp>
                  <Prp Name="PPG Has Entry Button Set">False</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="per5">
            <Prps>
              <Prp Name="Column span">4</Prp>
              <Prp Name="Visible">False</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Height">32px</Prp>
              <Prp Name="Width">4%</Prp>
              <Prp Name="Cell row">3</Prp>
              <Prp Name="Prompt">%</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFSpacer" Name="Spacer91" />
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell8">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Width">23%</Prp>
              <Prp Name="Cell row">4</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFSpacer" Name="Spacer5" />
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell10">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Width">2%</Prp>
              <Prp Name="Cell row">4</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFSpacer" Name="Spacer8" />
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell34">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Width">23%</Prp>
              <Prp Name="Cell row">4</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFSpacer" Name="Spacer16" />
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell35">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Width">10%</Prp>
              <Prp Name="Cell row">4</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFSpacer" Name="Spacer17" />
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell39">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Width">23%</Prp>
              <Prp Name="Cell row">4</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFSpacer" Name="Spacer18" />
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell42">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Width">23%</Prp>
              <Prp Name="Cell row">4</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFSpacer" Name="Spacer19" />
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell43">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Width">23%</Prp>
              <Prp Name="Cell row">4</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFSpacer" Name="Spacer20" />
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell44">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Width">23%</Prp>
              <Prp Name="Cell row">4</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFSpacer" Name="Spacer21" />
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell46">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Width">23%</Prp>
              <Prp Name="Cell row">4</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFSpacer" Name="Spacer22" />
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell51" DSrc="3" DFld="33" DCnt="1" DTyp="6">
            <Prps>
              <Prp Name="Column span">5</Prp>
              <Prp Name="Visible">False</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Padding">5px</Prp>
              <Prp Name="Height">39px</Prp>
              <Prp Name="Width">23%</Prp>
              <Prp Name="Cell row">5</Prp>
              <Prp Name="Prompt">Total Cholesterol</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFList" Name="SimTC" DSrc="3" DFld="34" DCnt="1" DTyp="6">
                <Prps>
                  <Prp Name="ListSource">3</Prp>
                  <Prp Name="Choices">130;160;190;220;250;280;310</Prp>
                  <Prp Name="ListCUI">15846</Prp>
                  <Prp Name="Multiple select">False</Prp>
                  <Prp Name="Style">1</Prp>
                  <Prp Name="Tooltip text">130=130;160=160;190=190;220=220;250=250;280=280;310=310</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell83">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Visible">False</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Height">32px</Prp>
              <Prp Name="Width">5%</Prp>
              <Prp Name="Cell row">5</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFLabel" Name="SignHF">
                <Prps>
                  <Prp Name="Caption">SignHF</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell70">
            <Prps>
              <Prp Name="Column span">3</Prp>
              <Prp Name="Visible">False</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Height">32px</Prp>
              <Prp Name="Width">3%</Prp>
              <Prp Name="Cell row">5</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFLabel" Name="DifHF">
                <Prps>
                  <Prp Name="Caption">HFDif</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell49" DSrc="3" DFld="35" DCnt="1" DTyp="6">
            <Prps>
              <Prp Name="Column span">9</Prp>
              <Prp Name="Visible">False</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Padding">5px</Prp>
              <Prp Name="Height">39px</Prp>
              <Prp Name="Width">23%</Prp>
              <Prp Name="Cell row">6</Prp>
              <Prp Name="Prompt">HDL</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFList" Name="SimHDL" DSrc="3" DFld="36" DCnt="1" DTyp="6">
                <Prps>
                  <Prp Name="ListSource">3</Prp>
                  <Prp Name="Choices">20;40;60;80;100</Prp>
                  <Prp Name="ListCUI">15848</Prp>
                  <Prp Name="Multiple select">False</Prp>
                  <Prp Name="Style">1</Prp>
                  <Prp Name="Tooltip text">20=20;40=40;60=60;80=80;100=100</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell54" DSrc="3" DFld="37" DCnt="1" DTyp="6">
            <Prps>
              <Prp Name="Column span">7</Prp>
              <Prp Name="Visible">False</Prp>
              <Prp Name="Component indent">5px</Prp>
              <Prp Name="Prompt indent">5px</Prp>
              <Prp Name="Height">8px</Prp>
              <Prp Name="Width">15%</Prp>
              <Prp Name="Cell row">7</Prp>
              <Prp Name="Prompt">DM</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFList" Name="SimDM" DSrc="3" DFld="38" DCnt="1" DTyp="6">
                <Prps>
                  <Prp Name="ListSource">3</Prp>
                  <Prp Name="Choices">Yes;No</Prp>
                  <Prp Name="ListCUI">15842</Prp>
                  <Prp Name="Multiple select">False</Prp>
                  <Prp Name="Tooltip text">Yes=1;No=0</Prp>
                  <Prp Name="Wrap options">False</Prp>
                  <Prp Name="Sizing">1</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell84" DSrc="3" DFld="39" DCnt="1" DTyp="6">
            <Prps>
              <Prp Name="Column span">2</Prp>
              <Prp Name="Visible">False</Prp>
              <Prp Name="Component indent">5px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Height">8px</Prp>
              <Prp Name="Width">23%</Prp>
              <Prp Name="Cell row">7</Prp>
              <Prp Name="Prompt">Smoker</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFList" Name="SimSM" DSrc="3" DFld="40" DCnt="1" DTyp="6">
                <Prps>
                  <Prp Name="ListSource">3</Prp>
                  <Prp Name="Choices">Yes;No</Prp>
                  <Prp Name="ListCUI">15887</Prp>
                  <Prp Name="Multiple select">False</Prp>
                  <Prp Name="Tooltip text">Yes=1;No=0</Prp>
                  <Prp Name="Sizing">1</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell21" DSrc="3" DFld="41" DCnt="1" DTyp="6">
            <Prps>
              <Prp Name="Column span">9</Prp>
              <Prp Name="Prompt width">125px</Prp>
              <Prp Name="Visible">False</Prp>
              <Prp Name="Back color">#FFFFFF</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">5px</Prp>
              <Prp Name="Padding">5px</Prp>
              <Prp Name="Width">15%</Prp>
              <Prp Name="Cell row">8</Prp>
              <Prp Name="Prompt">Modifiable Risk Factors for CVD</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFList" Name="ModifiableRisk" DSrc="3" DFld="42" DCnt="1" DTyp="6">
                <Prps>
                  <Prp Name="ListSource">3</Prp>
                  <Prp Name="Choices">Blood Pressure (goal SBP &lt; 130);Cholesterol control;Smoking counseling;Alcohol reduction;Other drug use;Physical activity;Nutrition;Obesity;Glycemic Control;None</Prp>
                  <Prp Name="ListCUI">15853</Prp>
                  <Prp Name="Tooltip text">Blood Pressure (goal SBP &lt; 130)=1;Cholesterol control=2;Smoking counseling=3;Alcohol reduction=4;Other drug use=5;Physical activity=6;Nutrition=7;Obesity=8;Glycemic Control=9;None=10</Prp>
                  <Prp Name="Sizing">1</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
        </Chld>
      </Cmpnt>
      <Cmpnt Type="EACSFComponents*.ACSFTableRow" Name="Row23">
        <Prps>
          <Prp Name="Rows">1</Prp>
          <Prp Name="Columns">1</Prp>
        </Prps>
        <Chld>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell45" DSrc="3" DFld="43" DCnt="1" DTyp="6">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Prompt width">125px</Prp>
              <Prp Name="Visible">False</Prp>
              <Prp Name="Back color">#FFFFFF</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">5px</Prp>
              <Prp Name="Padding">5px</Prp>
              <Prp Name="Width">89%</Prp>
              <Prp Name="Cell row">1</Prp>
              <Prp Name="Prompt">Screening Criteria</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFList" Name="Screening" DSrc="3" DFld="44" DCnt="1" DTyp="6">
                <Prps>
                  <Prp Name="ListSource">3</Prp>
                  <Prp Name="Choices">Obesity;Family Hx of CVD;HTN;HLD;Tobacco\Drug\Alcohol;DM;Pre-DM;Other;None</Prp>
                  <Prp Name="ListCUI">15817</Prp>
                  <Prp Name="Tooltip text">Obesity=1;Family Hx of CVD=2;HTN=4;HLD=8;Tobacco\Drug\Alcohol=16;DM=32;Pre-DM=64;Other=128;None=256</Prp>
                  <Prp Name="Sizing">1</Prp>
                  <Prp Name="Layout">1</Prp>
                  <Prp Name="Columns">5</Prp>
                  <Prp Name="Arrangement">2</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
        </Chld>
      </Cmpnt>
      <Cmpnt Type="EACSFComponents*.ACSFTableRow" Name="Row14">
        <Prps>
          <Prp Name="Rows">1</Prp>
          <Prp Name="Columns">1</Prp>
        </Prps>
        <Chld>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell22" DSrc="3" DFld="45" DCnt="1" DTyp="6">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Prompt width">125px</Prp>
              <Prp Name="Visible">False</Prp>
              <Prp Name="Back color">#FFFFFF</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">5px</Prp>
              <Prp Name="Padding">5px</Prp>
              <Prp Name="Cell row">1</Prp>
              <Prp Name="Prompt">Risk Enhancers</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFList" Name="RiskEnhancers" DSrc="3" DFld="46" DCnt="1" DTyp="6">
                <Prps>
                  <Prp Name="ListSource">3</Prp>
                  <Prp Name="Choices">Family Hx of Premature ASCVD (male &lt; 55 or female &lt; 65);Primary hypercholesterolemia (LDL160-189) or (Non-HDL 190-219);Metabolic Syndrome;CKD 3 to 4 (eGFR 15-59);Chronic inflammatory conditions (RA,Lupus, HIV, or Psoriasis);Hx of premature menopause (before age 40);Hx of preeclampsia;South Asian Ancestry;Primary Hypertriglyceridemia (&gt;175 mg/dl);Elevated Hs-CRP (&gt;2.0 mg/L);Elevated Lipoprotein(a) (&gt;50 mg/dl);Elevated apolipoprotein B (&gt;130 mg/dL);Ankle-brachial index (&lt;0.9);None</Prp>
                  <Prp Name="ListCUI">15854</Prp>
                  <Prp Name="Tooltip text">Family Hx of Premature ASCVD (male &lt; 55 or female &lt; 65)=1;Primary hypercholesterolemia (LDL160-189) or (Non-HDL 190-219)=2;Metabolic Syndrome=3;CKD 3 to 4 (eGFR 15-59)=4;Chronic inflammatory conditions (RA,Lupus, HIV, or Psoriasis)=5;Hx of premature menopause (before age 40)=6;Hx of preeclampsia=7;South Asian Ancestry=8;Primary Hypertriglyceridemia (&gt;175 mg/dl)=9;Elevated Hs-CRP (&gt;2.0 mg/L)=10;Elevated Lipoprotein(a) (&gt;50 mg/dl)=11;Elevated apolipoprotein B (&gt;130 mg/dL)=12;Ankle-brachial index (&lt;0.9)=13;None=14</Prp>
                  <Prp Name="Sizing">1</Prp>
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
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell6" DSrc="3" DFld="47" DCnt="1" DTyp="0">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Prompt width">125px</Prp>
              <Prp Name="Visible">False</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">5px</Prp>
              <Prp Name="Padding">5px</Prp>
              <Prp Name="Cell row">1</Prp>
              <Prp Name="Prompt">Cholesterol</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFChrontrol" Name="Field0" DSrc="3" DFld="48" DCnt="1" DTyp="0">
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
      <Cmpnt Type="EACSFComponents*.ACSFTableRow" Name="Row7">
        <Prps>
          <Prp Name="Rows">3</Prp>
          <Prp Name="Columns">5</Prp>
        </Prps>
        <Chld>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell18">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">10px</Prp>
              <Prp Name="Prompt indent">10px</Prp>
              <Prp Name="Height">38px</Prp>
              <Prp Name="Width">20%</Prp>
              <Prp Name="Cell row">1</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFLabel" Name="Label1">
                <Prps>
                  <Prp Name="Font">Arial;16pt;bold;normal;false;false;#000000</Prp>
                  <Prp Name="Caption">Charges</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Space5">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Height">38px</Prp>
              <Prp Name="Width">15%</Prp>
              <Prp Name="Cell row">1</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFSpacer" Name="Spacer1" />
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell5">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Visible">False</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Height">38px</Prp>
              <Prp Name="Width">15%</Prp>
              <Prp Name="Cell row">1</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFSpacer" Name="Spacer0" />
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell23" DSrc="3" DFld="49" DCnt="1" DTyp="6">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Prompt width">125px</Prp>
              <Prp Name="Visible">False</Prp>
              <Prp Name="Back color">#FFFFFF</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Padding">5px</Prp>
              <Prp Name="Height">38px</Prp>
              <Prp Name="Width">11.5%</Prp>
              <Prp Name="Cell row">1</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFList" Name="ASCVDRiskAssessment" DSrc="3" DFld="50" DCnt="1" DTyp="6">
                <Prps>
                  <Prp Name="ListSource">3</Prp>
                  <Prp Name="Choices">ASCVD Risk Assessment</Prp>
                  <Prp Name="ListCUI">15839</Prp>
                  <Prp Name="Tooltip text">ASCVD Risk Assessment=G0357</Prp>
                  <Prp Name="Sizing">1</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell0">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Height">38px</Prp>
              <Prp Name="Width">73%</Prp>
              <Prp Name="Cell row">1</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFLabel" Name="ASCVDRiskAssessText">
                <Prps>
                  <Prp Name="Caption">ASCVD Risk Assessment Requires: Screening Criteria, No Prior Hx of ASCVD, Lipid Panel 12 Months, Modifiable Risk Factors, and Risk Enhancer if eligible. The charge must be attached to EM Visit and 1 per year per practitioner. May be added with G2211</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell29">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Width">20%</Prp>
              <Prp Name="Cell row">2</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFSpacer" Name="Spacer14" />
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell31">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Visible">False</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Height">38px</Prp>
              <Prp Name="Width">1.5%</Prp>
              <Prp Name="Cell row">2</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFLabel" Name="Label3">
                <Prps>
                  <Prp Name="Caption">Lipid Panel &gt; 12 Months</Prp>
                  <Prp Name="Label type">7</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell47">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Width">1.5%</Prp>
              <Prp Name="Cell row">2</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFSpacer" Name="Spacer23" />
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell48">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Width">11.5%</Prp>
              <Prp Name="Cell row">2</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFSpacer" Name="Spacer25" />
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell50">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Width">73%</Prp>
              <Prp Name="Cell row">2</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFSpacer" Name="Spacer27" />
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell38">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">10px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Height">38px</Prp>
              <Prp Name="Width">20%</Prp>
              <Prp Name="Cell row">3</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFLabel" Name="Label5">
                <Prps>
                  <Prp Name="Font">Arial;16pt;bold;normal;false;false;#000000</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell30">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Width">9%</Prp>
              <Prp Name="Cell row">3</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFSpacer" Name="Spacer6" />
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell32">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Visible">False</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Width">1.5%</Prp>
              <Prp Name="Cell row">3</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFSpacer" Name="Spacer7" />
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell36" DSrc="3" DFld="51" DCnt="1" DTyp="6">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Prompt width">125px</Prp>
              <Prp Name="Visible">False</Prp>
              <Prp Name="Back color">#FFFFFF</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Padding">5px</Prp>
              <Prp Name="Height">38px</Prp>
              <Prp Name="Width">11.5%</Prp>
              <Prp Name="Cell row">3</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFList" Name="ASCVDRiskManagement" DSrc="3" DFld="52" DCnt="1" DTyp="6">
                <Prps>
                  <Prp Name="ListSource">3</Prp>
                  <Prp Name="Choices">ASCVD Risk Management</Prp>
                  <Prp Name="ListCUI">15973</Prp>
                  <Prp Name="Tooltip text">ASCVD Risk Management=G0358</Prp>
                  <Prp Name="Sizing">1</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell37">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Height">38px</Prp>
              <Prp Name="Width">73%</Prp>
              <Prp Name="Cell row">3</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFLabel" Name="ASCVDRiskManText">
                <Prps>
                  <Prp Name="Caption">ASCVD Risk Management Requires: Intermediate or Higher CVD Risk. Address Modfiable Risk Factors and Risk Enhancers. Establish Plan, Medication Management (ABCS - ASA, Blood Pressure Control, Cholesterol Control, and Smoking Cessation).  The charge may be billed 1 per month per practitioner and with G2211</Prp>
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
          <Cmpnt Type="EACSFComponents*.ACSFCell" Name="Cell25">
            <Prps>
              <Prp Name="Column span">1</Prp>
              <Prp Name="Component indent">1px</Prp>
              <Prp Name="Prompt indent">1px</Prp>
              <Prp Name="Cell row">1</Prp>
            </Prps>
            <Chld>
              <Cmpnt Type="EACSFComponents*.ACSFLabel" Name="Label2">
                <Prps>
                  <Prp Name="Caption">Circulation. 2024;149:430–449. DOI: 10.1161/CIRCULATIONAHA.123.067626</Prp>
                </Prps>
              </Cmpnt>
            </Chld>
          </Cmpnt>
        </Chld>
      </Cmpnt>
    </Chld>
  </Cmpnt>
  <FormScripts ScriptVersion="1.0">
    <Script Name="SimHF_ValueChanged" ProcType="3" CreationType="2" ParamCount="0" Component="">
      <Action ActionType="1" Name="Sim" Key="Condition1">
        <ActionProperty Name="IfConnectionLogic" Value="1" />
        <Checks>
          <Check CheckType="1" Name="Check1" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckPropComponentID" Value="SimTitle" />
            <CheckProperty Name="IfCheckPropRealComponentID" Value="Cell99" />
            <CheckProperty Name="IfCheckPropProperty" Value="Visible" />
            <CheckProperty Name="IfCheckPropValue" Value="True" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="6" Name="HFDif" Key="Action6">
            <ActionProperty Name="CalculateExpression" Value="(SimHF-HF10) " />
            <ActionProperty Name="CalculateRequireAllVariables" Value="True" />
            <ActionProperty Name="CalculateVersion" Value="1" />
            <ActionProperty Name="SetValueRealComponentID" Value="DifHF" />
            <ActionProperty Name="CalculateClearWhenMissingVars" Value="False" />
            <ActionProperty Name="SetValueComponentID" Value="DifHF" />
          </Action>
          <Action ActionType="1" Name="HFDif &gt; 0 " Key="Condition2">
            <ActionProperty Name="IfConnectionLogic" Value="1" />
            <Checks>
              <Check CheckType="1" Name="Check1" Key="Check1" CheckNum="1">
                <CheckProperty Name="IfCheckPropComponentID" Value="DifHF" />
                <CheckProperty Name="IfCheckPropRealComponentID" Value="DifHF" />
                <CheckProperty Name="IfCheckPropProperty" Value="Caption" />
                <CheckProperty Name="IfCheckPropValue" Value="0" />
              </Check>
            </Checks>
            <TrueBranch>
              <Action ActionType="6" Name="HFSignNull" Key="Action1">
                <ActionProperty Name="CalculateExpression" Value="0" />
                <ActionProperty Name="CalculateRequireAllVariables" Value="False" />
                <ActionProperty Name="CalculateVersion" Value="1" />
                <ActionProperty Name="SetValueRealComponentID" Value="SignHF" />
                <ActionProperty Name="CalculateClearWhenMissingVars" Value="False" />
                <ActionProperty Name="SetValueComponentID" Value="SignHF" />
              </Action>
            </TrueBranch>
            <FalseBranch>
              <Action ActionType="6" Name="Action1" Key="Action7">
                <ActionProperty Name="CalculateExpression" Value="(SimHF-HF10+0.001)/(((SimHF-HF10+0.001) ^ 2)^(1/2))" />
                <ActionProperty Name="CalculateRequireAllVariables" Value="True" />
                <ActionProperty Name="CalculateVersion" Value="1" />
                <ActionProperty Name="SetValueRealComponentID" Value="SignHF" />
                <ActionProperty Name="CalculateClearWhenMissingVars" Value="False" />
                <ActionProperty Name="SetValueComponentID" Value="SignHF" />
              </Action>
            </FalseBranch>
          </Action>
        </TrueBranch>
        <FalseBranch>
          <Action ActionType="6" Name="HFSignNull" Key="Action2">
            <ActionProperty Name="CalculateExpression" Value="0" />
            <ActionProperty Name="CalculateRequireAllVariables" Value="False" />
            <ActionProperty Name="CalculateVersion" Value="1" />
            <ActionProperty Name="SetValueRealComponentID" Value="SignHF" />
            <ActionProperty Name="CalculateClearWhenMissingVars" Value="False" />
            <ActionProperty Name="SetValueComponentID" Value="SignHF" />
          </Action>
        </FalseBranch>
      </Action>
      <Action ActionType="1" Name="Flag" Key="Condition3">
        <ActionProperty Name="IfConnectionLogic" Value="1" />
        <Checks>
          <Check CheckType="1" Name="Check1" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckPropComponentID" Value="SignHF" />
            <CheckProperty Name="IfCheckPropRealComponentID" Value="SignHF" />
            <CheckProperty Name="IfCheckPropProperty" Value="Caption" />
            <CheckProperty Name="IfCheckPropValue" Value="-1" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="4" Name="Reduction" Key="Action3">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell28" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="#80FF80" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimHF" />
          </Action>
          <Action ActionType="4" Name="per5" Key="Action9">
            <ActionProperty Name="SetPropertyRealComponentID" Value="per5" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="#80FF80" />
            <ActionProperty Name="SetPropertyComponentID" Value="per5" />
          </Action>
        </TrueBranch>
        <FalseBranch>
          <Action ActionType="1" Name="Condition4" Key="Condition4">
            <ActionProperty Name="IfConnectionLogic" Value="1" />
            <Checks>
              <Check CheckType="1" Name="Check1" Key="Check1" CheckNum="1">
                <CheckProperty Name="IfCheckPropComponentID" Value="SignHF" />
                <CheckProperty Name="IfCheckPropRealComponentID" Value="SignHF" />
                <CheckProperty Name="IfCheckPropProperty" Value="Caption" />
                <CheckProperty Name="IfCheckPropValue" Value="1" />
              </Check>
            </Checks>
            <TrueBranch>
              <Action ActionType="4" Name="Increase" Key="Action4">
                <ActionProperty Name="SetPropertyRealComponentID" Value="Cell28" />
                <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                <ActionProperty Name="SetPropertyPropertyValue" Value="#FF0000" />
                <ActionProperty Name="SetPropertyComponentID" Value="SimHF" />
              </Action>
              <Action ActionType="4" Name="per5" Key="Action10">
                <ActionProperty Name="SetPropertyRealComponentID" Value="per5" />
                <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                <ActionProperty Name="SetPropertyPropertyValue" Value="#80FF80" />
                <ActionProperty Name="SetPropertyComponentID" Value="per5" />
              </Action>
            </TrueBranch>
            <FalseBranch>
              <Action ActionType="1" Name="Condition4" Key="Condition5">
                <ActionProperty Name="IfConnectionLogic" Value="1" />
                <Checks>
                  <Check CheckType="1" Name="Check1" Key="Check1" CheckNum="1">
                    <CheckProperty Name="IfCheckPropComponentID" Value="SignHF" />
                    <CheckProperty Name="IfCheckPropRealComponentID" Value="SignHF" />
                    <CheckProperty Name="IfCheckPropProperty" Value="Caption" />
                    <CheckProperty Name="IfCheckPropValue" Value="0" />
                  </Check>
                </Checks>
                <TrueBranch>
                  <Action ActionType="4" Name="Null" Key="Action8">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="Cell28" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                    <ActionProperty Name="SetPropertyPropertyValue" Value="#FFFFFF" />
                    <ActionProperty Name="SetPropertyComponentID" Value="SimHF" />
                  </Action>
                  <Action ActionType="4" Name="per5" Key="Action11">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="per5" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                    <ActionProperty Name="SetPropertyPropertyValue" Value="#FFFFFF" />
                    <ActionProperty Name="SetPropertyComponentID" Value="per5" />
                  </Action>
                </TrueBranch>
                <FalseBranch>
                  <Action ActionType="4" Name="Null" Key="Action5">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="Cell28" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                    <ActionProperty Name="SetPropertyPropertyValue" Value="#FFFFFF" />
                    <ActionProperty Name="SetPropertyComponentID" Value="SimHF" />
                  </Action>
                  <Action ActionType="4" Name="per5" Key="Action12">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="per5" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                    <ActionProperty Name="SetPropertyPropertyValue" Value="#FFFFFF" />
                    <ActionProperty Name="SetPropertyComponentID" Value="per5" />
                  </Action>
                </FalseBranch>
              </Action>
            </FalseBranch>
          </Action>
        </FalseBranch>
      </Action>
    </Script>
    <Script Name="Smoker_ValueChanged" ProcType="3" CreationType="2" ParamCount="0" Component="">
      <Action ActionType="1" Name="SMCheck" Key="Condition1">
        <ActionProperty Name="IfConnectionLogicType" Value="1" />
        <ActionProperty Name="IfConnectionLogic" Value="1" />
        <Checks>
          <Check CheckType="2" Name="Check1" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="Smoking counseling$$C6$$" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="3" Name="Action17" Key="Action1">
            <ActionProperty Name="SetValueRealComponentID" Value="SimSM" />
            <ActionProperty Name="SetValueOptions" Value="1" />
            <ActionProperty Name="SetValueWhich" Value="1" />
            <ActionProperty Name="SetValueComponentID" Value="SimSM" />
            <ActionProperty Name="SetValueComponentValue" Value="No$$C6$$" />
          </Action>
        </TrueBranch>
        <FalseBranch>
          <Action ActionType="1" Name="Condition6" Key="Condition2">
            <ActionProperty Name="IfConnectionLogic" Value="1" />
            <Checks>
              <Check CheckType="2" Name="Check1" Key="Check1" CheckNum="1">
                <CheckProperty Name="IfCheckValueWhich" Value="1" />
                <CheckProperty Name="IfCheckValueComponentID" Value="Smoker" />
                <CheckProperty Name="IfCheckValueRealComponentID" Value="Smoker" />
                <CheckProperty Name="IfCheckValueOperator" Value="1" />
                <CheckProperty Name="IfCheckValueValue" Value="Yes$$C6$$" />
              </Check>
            </Checks>
            <TrueBranch>
              <Action ActionType="3" Name="Action17" Key="Action2">
                <ActionProperty Name="SetValueRealComponentID" Value="SimSM" />
                <ActionProperty Name="SetValueOptions" Value="1" />
                <ActionProperty Name="SetValueWhich" Value="1" />
                <ActionProperty Name="SetValueComponentID" Value="SimSM" />
                <ActionProperty Name="SetValueComponentValue" Value="Yes$$C6$$" />
              </Action>
            </TrueBranch>
            <FalseBranch>
              <Action ActionType="3" Name="Action17" Key="Action3">
                <ActionProperty Name="SetValueRealComponentID" Value="SimSM" />
                <ActionProperty Name="SetValueOptions" Value="1" />
                <ActionProperty Name="SetValueWhich" Value="1" />
                <ActionProperty Name="SetValueComponentID" Value="SimSM" />
                <ActionProperty Name="SetValueComponentValue" Value="No$$C6$$" />
              </Action>
            </FalseBranch>
          </Action>
        </FalseBranch>
      </Action>
    </Script>
    <Script Name="SimCVD_ValueChanged" ProcType="3" CreationType="2" ParamCount="0" Component="">
      <Action ActionType="1" Name="Sim" Key="Condition1">
        <ActionProperty Name="IfConnectionLogic" Value="1" />
        <Checks>
          <Check CheckType="1" Name="Check1" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckPropComponentID" Value="SimTitle" />
            <CheckProperty Name="IfCheckPropRealComponentID" Value="Cell99" />
            <CheckProperty Name="IfCheckPropProperty" Value="Visible" />
            <CheckProperty Name="IfCheckPropValue" Value="True" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="6" Name="DifCVD" Key="Action2">
            <ActionProperty Name="CalculateExpression" Value="SimCVD -  CVD10  " />
            <ActionProperty Name="CalculateRequireAllVariables" Value="True" />
            <ActionProperty Name="CalculateVersion" Value="1" />
            <ActionProperty Name="SetValueRealComponentID" Value="DifCVD" />
            <ActionProperty Name="CalculateClearWhenMissingVars" Value="False" />
            <ActionProperty Name="SetValueComponentID" Value="DifCVD" />
          </Action>
          <Action ActionType="1" Name="DifCVD &gt; 0 " Key="Condition2">
            <ActionProperty Name="IfConnectionLogic" Value="1" />
            <Checks>
              <Check CheckType="1" Name="Check1" Key="Check1" CheckNum="1">
                <CheckProperty Name="IfCheckPropComponentID" Value="DifCVD" />
                <CheckProperty Name="IfCheckPropRealComponentID" Value="DifCVD" />
                <CheckProperty Name="IfCheckPropProperty" Value="Caption" />
                <CheckProperty Name="IfCheckPropValue" Value="0" />
              </Check>
            </Checks>
            <TrueBranch>
              <Action ActionType="6" Name="HFSignNull" Key="Action1">
                <ActionProperty Name="CalculateExpression" Value="0" />
                <ActionProperty Name="CalculateRequireAllVariables" Value="False" />
                <ActionProperty Name="CalculateVersion" Value="1" />
                <ActionProperty Name="SetValueRealComponentID" Value="SignCVD" />
                <ActionProperty Name="CalculateClearWhenMissingVars" Value="False" />
                <ActionProperty Name="SetValueComponentID" Value="SignCVD" />
              </Action>
            </TrueBranch>
            <FalseBranch>
              <Action ActionType="6" Name="Action1" Key="Action16">
                <ActionProperty Name="CalculateExpression" Value="(SimCVD-CVD10+0.001)/(((SimCVD-CVD10+0.001) ^ 2)^(1/2))" />
                <ActionProperty Name="CalculateRequireAllVariables" Value="True" />
                <ActionProperty Name="CalculateVersion" Value="1" />
                <ActionProperty Name="SetValueRealComponentID" Value="SignCVD" />
                <ActionProperty Name="CalculateClearWhenMissingVars" Value="False" />
                <ActionProperty Name="SetValueComponentID" Value="SignCVD" />
              </Action>
            </FalseBranch>
          </Action>
        </TrueBranch>
        <FalseBranch>
          <Action ActionType="6" Name="HFSignNull" Key="Action4">
            <ActionProperty Name="CalculateExpression" Value="0" />
            <ActionProperty Name="CalculateRequireAllVariables" Value="False" />
            <ActionProperty Name="CalculateVersion" Value="1" />
            <ActionProperty Name="SetValueRealComponentID" Value="SignCVD" />
            <ActionProperty Name="CalculateClearWhenMissingVars" Value="False" />
            <ActionProperty Name="SetValueComponentID" Value="SignCVD" />
          </Action>
        </FalseBranch>
      </Action>
      <Action ActionType="1" Name="Flag Decrease" Key="Condition3">
        <ActionProperty Name="IfConnectionLogic" Value="1" />
        <Checks>
          <Check CheckType="1" Name="Check1" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckPropComponentID" Value="SignCVD" />
            <CheckProperty Name="IfCheckPropRealComponentID" Value="SignCVD" />
            <CheckProperty Name="IfCheckPropProperty" Value="Caption" />
            <CheckProperty Name="IfCheckPropValue" Value="-1" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="4" Name="SimCVA" Key="Action8">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell27" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="#80FF80" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimCVA" />
          </Action>
          <Action ActionType="4" Name="SimCHD" Key="Action9">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell26" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="#80FF80" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimCHD" />
          </Action>
          <Action ActionType="4" Name="SimCVD" Key="Action10">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell20" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="#80FF80" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimCVD" />
          </Action>
          <Action ActionType="4" Name="SimASCVD" Key="Action7">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell19" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="#80FF80" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimASCVd" />
          </Action>
          <Action ActionType="4" Name="per1" Key="Action21">
            <ActionProperty Name="SetPropertyRealComponentID" Value="per1" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="#80FF80" />
            <ActionProperty Name="SetPropertyComponentID" Value="per1" />
          </Action>
          <Action ActionType="4" Name="per2" Key="Action22">
            <ActionProperty Name="SetPropertyRealComponentID" Value="per2" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="#80FF80" />
            <ActionProperty Name="SetPropertyComponentID" Value="per2" />
          </Action>
          <Action ActionType="4" Name="per3" Key="Action23">
            <ActionProperty Name="SetPropertyRealComponentID" Value="per3" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="#80FF80" />
            <ActionProperty Name="SetPropertyComponentID" Value="per3" />
          </Action>
          <Action ActionType="4" Name="per4" Key="Action24">
            <ActionProperty Name="SetPropertyRealComponentID" Value="per4" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="#80FF80" />
            <ActionProperty Name="SetPropertyComponentID" Value="per4" />
          </Action>
        </TrueBranch>
        <FalseBranch>
          <Action ActionType="1" Name="Increase" Key="Condition4">
            <ActionProperty Name="IfConnectionLogic" Value="2" />
            <Checks>
              <Check CheckType="1" Name="Check1" Key="Check2" CheckNum="2">
                <CheckProperty Name="IfCheckPropComponentID" Value="SignCVD" />
                <CheckProperty Name="IfCheckPropRealComponentID" Value="SignCVD" />
                <CheckProperty Name="IfCheckPropProperty" Value="Caption" />
                <CheckProperty Name="IfCheckPropValue" Value="1" />
              </Check>
            </Checks>
            <TrueBranch>
              <Action ActionType="4" Name="SimASCVD" Key="Action11">
                <ActionProperty Name="SetPropertyRealComponentID" Value="Cell19" />
                <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                <ActionProperty Name="SetPropertyPropertyValue" Value="#FF0000" />
                <ActionProperty Name="SetPropertyComponentID" Value="SimASCVd" />
              </Action>
              <Action ActionType="4" Name="SimCVA" Key="Action12">
                <ActionProperty Name="SetPropertyRealComponentID" Value="Cell27" />
                <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                <ActionProperty Name="SetPropertyPropertyValue" Value="#FF0000" />
                <ActionProperty Name="SetPropertyComponentID" Value="SimCVA" />
              </Action>
              <Action ActionType="4" Name="SimCHD" Key="Action13">
                <ActionProperty Name="SetPropertyRealComponentID" Value="Cell26" />
                <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                <ActionProperty Name="SetPropertyPropertyValue" Value="#FF0000" />
                <ActionProperty Name="SetPropertyComponentID" Value="SimCHD" />
              </Action>
              <Action ActionType="4" Name="per3" Key="Action26">
                <ActionProperty Name="SetPropertyRealComponentID" Value="per3" />
                <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                <ActionProperty Name="SetPropertyPropertyValue" Value="#FF0000" />
                <ActionProperty Name="SetPropertyComponentID" Value="per3" />
              </Action>
              <Action ActionType="4" Name="per1" Key="Action27">
                <ActionProperty Name="SetPropertyRealComponentID" Value="per1" />
                <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                <ActionProperty Name="SetPropertyPropertyValue" Value="#FF0000" />
                <ActionProperty Name="SetPropertyComponentID" Value="per1" />
              </Action>
              <Action ActionType="4" Name="per2" Key="Action28">
                <ActionProperty Name="SetPropertyRealComponentID" Value="per2" />
                <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                <ActionProperty Name="SetPropertyPropertyValue" Value="#FF0000" />
                <ActionProperty Name="SetPropertyComponentID" Value="per2" />
              </Action>
              <Action ActionType="4" Name="per4" Key="Action29">
                <ActionProperty Name="SetPropertyRealComponentID" Value="per4" />
                <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                <ActionProperty Name="SetPropertyPropertyValue" Value="#FF0000" />
                <ActionProperty Name="SetPropertyComponentID" Value="per4" />
              </Action>
            </TrueBranch>
            <FalseBranch>
              <Action ActionType="1" Name="Null" Key="Condition5">
                <ActionProperty Name="IfConnectionLogic" Value="2" />
                <Checks>
                  <Check CheckType="1" Name="Check1" Key="Check2" CheckNum="2">
                    <CheckProperty Name="IfCheckPropComponentID" Value="SignCVD" />
                    <CheckProperty Name="IfCheckPropRealComponentID" Value="SignCVD" />
                    <CheckProperty Name="IfCheckPropProperty" Value="Caption" />
                    <CheckProperty Name="IfCheckPropValue" Value="0" />
                  </Check>
                </Checks>
                <TrueBranch>
                  <Action ActionType="4" Name="SimASCVD" Key="Action3">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="Cell19" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                    <ActionProperty Name="SetPropertyPropertyValue" Value="#FFFFFF" />
                    <ActionProperty Name="SetPropertyComponentID" Value="SimASCVd" />
                  </Action>
                  <Action ActionType="4" Name="SimCVD" Key="Action5">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="Cell20" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                    <ActionProperty Name="SetPropertyPropertyValue" Value="#FFFFFF" />
                    <ActionProperty Name="SetPropertyComponentID" Value="SimCVD" />
                  </Action>
                  <Action ActionType="4" Name="SimCHD" Key="Action6">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="Cell26" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                    <ActionProperty Name="SetPropertyPropertyValue" Value="#FFFFFF" />
                    <ActionProperty Name="SetPropertyComponentID" Value="SimCHD" />
                  </Action>
                  <Action ActionType="4" Name="SimCVA" Key="Action15">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="Cell27" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                    <ActionProperty Name="SetPropertyPropertyValue" Value="#FFFFFF" />
                    <ActionProperty Name="SetPropertyComponentID" Value="SimCVA" />
                  </Action>
                  <Action ActionType="4" Name="per3" Key="Action31">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="per3" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                    <ActionProperty Name="SetPropertyComponentID" Value="per3" />
                  </Action>
                  <Action ActionType="4" Name="per2" Key="Action32">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="per2" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                    <ActionProperty Name="SetPropertyComponentID" Value="per2" />
                  </Action>
                  <Action ActionType="4" Name="per4" Key="Action33">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="per4" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                    <ActionProperty Name="SetPropertyComponentID" Value="per4" />
                  </Action>
                  <Action ActionType="4" Name="per1" Key="Action34">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="per1" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                    <ActionProperty Name="SetPropertyComponentID" Value="per1" />
                  </Action>
                </TrueBranch>
                <FalseBranch>
                  <Action ActionType="4" Name="SimASCVD" Key="Action17">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="Cell19" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                    <ActionProperty Name="SetPropertyPropertyValue" Value="#FFFFFF" />
                    <ActionProperty Name="SetPropertyComponentID" Value="SimASCVd" />
                  </Action>
                  <Action ActionType="4" Name="SimCVA" Key="Action18">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="Cell27" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                    <ActionProperty Name="SetPropertyPropertyValue" Value="#FFFFFF" />
                    <ActionProperty Name="SetPropertyComponentID" Value="SimCVA" />
                  </Action>
                  <Action ActionType="4" Name="SimCHD" Key="Action19">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="Cell26" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                    <ActionProperty Name="SetPropertyPropertyValue" Value="#FFFFFF" />
                    <ActionProperty Name="SetPropertyComponentID" Value="SimCHD" />
                  </Action>
                  <Action ActionType="4" Name="SimCVD" Key="Action20">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="Cell20" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                    <ActionProperty Name="SetPropertyPropertyValue" Value="#FFFFFF" />
                    <ActionProperty Name="SetPropertyComponentID" Value="SimCVD" />
                  </Action>
                </FalseBranch>
              </Action>
            </FalseBranch>
          </Action>
        </FalseBranch>
      </Action>
    </Script>
    <Script Name="ARootComponent_BeforeDataSaved" ProcType="3" CreationType="2" ParamCount="0" Component="">
      <Action ActionType="1" Name="ModVisClear" Key="Condition2">
        <ActionProperty Name="IfConnectionLogic" Value="1" />
        <Checks>
          <Check CheckType="1" Name="Check1" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckPropComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckPropRealComponentID" Value="Cell21" />
            <CheckProperty Name="IfCheckPropProperty" Value="Visible" />
            <CheckProperty Name="IfCheckPropValue" Value="False" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="3" Name="Action2" Key="Action2">
            <ActionProperty Name="SetValueRealComponentID" Value="ModifiableRisk" />
            <ActionProperty Name="SetValueOptions" Value="1" />
            <ActionProperty Name="SuppressValueChangedEvents" Value="1" />
            <ActionProperty Name="SetValueWhich" Value="1" />
            <ActionProperty Name="SetValueComponentID" Value="ModifiableRisk" />
            <ActionProperty Name="SetValueComponentValue" Value="$$C6$$" />
          </Action>
        </TrueBranch>
      </Action>
      <Action ActionType="1" Name="RiskVisClear" Key="Condition1">
        <ActionProperty Name="IfConnectionLogic" Value="1" />
        <Checks>
          <Check CheckType="1" Name="Check1" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckPropComponentID" Value="RiskEnhancers" />
            <CheckProperty Name="IfCheckPropRealComponentID" Value="Cell22" />
            <CheckProperty Name="IfCheckPropProperty" Value="Visible" />
            <CheckProperty Name="IfCheckPropValue" Value="False" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="3" Name="Clear" Key="Action1">
            <ActionProperty Name="SetValueRealComponentID" Value="RiskEnhancers" />
            <ActionProperty Name="SetValueOptions" Value="1" />
            <ActionProperty Name="SetValueWhich" Value="1" />
            <ActionProperty Name="SetValueComponentID" Value="RiskEnhancers" />
            <ActionProperty Name="SetValueComponentValue" Value="$$C6$$" />
          </Action>
        </TrueBranch>
      </Action>
      <Action ActionType="1" Name="SimVisClear" Key="Condition3">
        <ActionProperty Name="IfConnectionLogic" Value="1" />
        <Checks>
          <Check CheckType="1" Name="Check1" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckPropComponentID" Value="SimTitle" />
            <CheckProperty Name="IfCheckPropRealComponentID" Value="Cell99" />
            <CheckProperty Name="IfCheckPropProperty" Value="Visible" />
            <CheckProperty Name="IfCheckPropValue" Value="False" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="3" Name="Action4" Key="Action4">
            <ActionProperty Name="SetValueRealComponentID" Value="SimCVD" />
            <ActionProperty Name="SetValueOptions" Value="1" />
            <ActionProperty Name="SetValueWhich" Value="1" />
            <ActionProperty Name="SetValueComponentID" Value="SimCVD" />
            <ActionProperty Name="SetValueComponentValue" Value="0$$C6$$" />
          </Action>
          <Action ActionType="3" Name="Action3" Key="Action3">
            <ActionProperty Name="SetValueRealComponentID" Value="SimASCVd" />
            <ActionProperty Name="SetValueOptions" Value="1" />
            <ActionProperty Name="SetValueWhich" Value="1" />
            <ActionProperty Name="SetValueComponentID" Value="SimASCVd" />
            <ActionProperty Name="SetValueComponentValue" Value="0$$C6$$" />
          </Action>
          <Action ActionType="3" Name="Action4" Key="Action5">
            <ActionProperty Name="SetValueRealComponentID" Value="SimCHD" />
            <ActionProperty Name="SetValueOptions" Value="1" />
            <ActionProperty Name="SetValueWhich" Value="1" />
            <ActionProperty Name="SetValueComponentID" Value="SimCHD" />
            <ActionProperty Name="SetValueComponentValue" Value="0$$C6$$" />
          </Action>
          <Action ActionType="3" Name="Action7" Key="Action7">
            <ActionProperty Name="SetValueRealComponentID" Value="SimCVA" />
            <ActionProperty Name="SetValueOptions" Value="1" />
            <ActionProperty Name="SetValueWhich" Value="1" />
            <ActionProperty Name="SetValueComponentID" Value="SimCVA" />
            <ActionProperty Name="SetValueComponentValue" Value="0$$C6$$" />
          </Action>
          <Action ActionType="3" Name="Action4" Key="Action6">
            <ActionProperty Name="SetValueRealComponentID" Value="SimHF" />
            <ActionProperty Name="SetValueOptions" Value="1" />
            <ActionProperty Name="SetValueWhich" Value="1" />
            <ActionProperty Name="SetValueComponentID" Value="SimHF" />
            <ActionProperty Name="SetValueComponentValue" Value="$$C6$$" />
          </Action>
        </TrueBranch>
      </Action>
    </Script>
    <Script Name="ARootComponent_AfterDataLoaded" ProcType="3" CreationType="2" ParamCount="0" Component="">
      <Action ActionType="1" Name="Screen" Key="Condition11">
        <ActionProperty Name="IfConnectionLogic" Value="1" />
        <Checks>
          <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckRuleID" Value="1" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="3" Name="Action1" Key="Action10">
            <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
            <ActionProperty Name="SetValueOptions" Value="1" />
            <ActionProperty Name="SetValueWhich" Value="1" />
            <ActionProperty Name="SetValueComponentID" Value="Screening" />
            <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C6$$" />
          </Action>
          <Action ActionType="1" Name="FamHx" Key="Condition12">
            <ActionProperty Name="IfConnectionLogic" Value="1" />
            <Checks>
              <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                <CheckProperty Name="IfCheckRuleID" Value="2" />
              </Check>
            </Checks>
            <TrueBranch>
              <Action ActionType="3" Name="Action2" Key="Action11">
                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                <ActionProperty Name="SetValueOptions" Value="1" />
                <ActionProperty Name="SetValueWhich" Value="1" />
                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                <ActionProperty Name="SetValueComponentValue" Value="Family Hx of CVD$$C5$$Obesity$$C6$$" />
              </Action>
              <Action ActionType="1" Name="HTN" Key="Condition13">
                <ActionProperty Name="IfConnectionLogic" Value="1" />
                <Checks>
                  <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                    <CheckProperty Name="IfCheckRuleID" Value="3" />
                  </Check>
                </Checks>
                <TrueBranch>
                  <Action ActionType="3" Name="Action3" Key="Action12">
                    <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                    <ActionProperty Name="SetValueOptions" Value="1" />
                    <ActionProperty Name="SetValueWhich" Value="1" />
                    <ActionProperty Name="SetValueComponentID" Value="Screening" />
                    <ActionProperty Name="SetValueComponentValue" Value="HTN$$C5$$Family Hx of CVD$$C5$$Obesity$$C6$$" />
                  </Action>
                  <Action ActionType="1" Name="HLD" Key="Condition14">
                    <ActionProperty Name="IfConnectionLogic" Value="1" />
                    <Checks>
                      <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                        <CheckProperty Name="IfCheckRuleID" Value="4" />
                      </Check>
                    </Checks>
                    <TrueBranch>
                      <Action ActionType="3" Name="Action4" Key="Action13">
                        <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                        <ActionProperty Name="SetValueOptions" Value="1" />
                        <ActionProperty Name="SetValueWhich" Value="1" />
                        <ActionProperty Name="SetValueComponentID" Value="Screening" />
                        <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$Family Hx of CVD$$C5$$HTN$$C5$$HLD$$C6$$" />
                      </Action>
                      <Action ActionType="1" Name="TAD" Key="Condition15">
                        <ActionProperty Name="IfConnectionLogic" Value="1" />
                        <Checks>
                          <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                            <CheckProperty Name="IfCheckRuleID" Value="5" />
                          </Check>
                        </Checks>
                        <TrueBranch>
                          <Action ActionType="3" Name="Action5" Key="Action15">
                            <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$Family Hx of CVD$$C5$$HTN$$C5$$HLD$$C5$$Tobacco\Drug\Alcohol$$C6$$" />
                          </Action>
                          <Action ActionType="1" Name="DM" Key="Condition16">
                            <ActionProperty Name="IfConnectionLogic" Value="1" />
                            <Checks>
                              <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                                <CheckProperty Name="IfCheckRuleID" Value="6" />
                              </Check>
                            </Checks>
                            <TrueBranch>
                              <Action ActionType="3" Name="Action6" Key="Action22">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$Family Hx of CVD$$C5$$HTN$$C5$$HLD$$C5$$Tobacco\Drug\Alcohol$$C5$$DM$$C6$$" />
                              </Action>
                            </TrueBranch>
                            <FalseBranch>
                              <Action ActionType="3" Name="Action6" Key="Action14">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$Family Hx of CVD$$C5$$HTN$$C5$$HLD$$C5$$Tobacco\Drug\Alcohol$$C6$$" />
                              </Action>
                            </FalseBranch>
                          </Action>
                        </TrueBranch>
                        <FalseBranch>
                          <Action ActionType="3" Name="Action5" Key="Action37">
                            <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$Family Hx of CVD$$C5$$HTN$$C5$$HLD$$C6$$" />
                          </Action>
                          <Action ActionType="1" Name="DM" Key="Condition17">
                            <ActionProperty Name="IfConnectionLogic" Value="1" />
                            <Checks>
                              <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                                <CheckProperty Name="IfCheckRuleID" Value="7" />
                              </Check>
                            </Checks>
                            <TrueBranch>
                              <Action ActionType="3" Name="Action6" Key="Action18">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$Family Hx of CVD$$C5$$HTN$$C5$$HLD$$C5$$DM$$C6$$" />
                              </Action>
                            </TrueBranch>
                            <FalseBranch>
                              <Action ActionType="3" Name="Action6" Key="Action17">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$Family Hx of CVD$$C5$$HTN$$C5$$HLD$$C6$$" />
                              </Action>
                            </FalseBranch>
                          </Action>
                        </FalseBranch>
                      </Action>
                    </TrueBranch>
                    <FalseBranch>
                      <Action ActionType="3" Name="Action4" Key="Action134">
                        <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                        <ActionProperty Name="SetValueOptions" Value="1" />
                        <ActionProperty Name="SetValueWhich" Value="1" />
                        <ActionProperty Name="SetValueComponentID" Value="Screening" />
                        <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$Family Hx of CVD$$C5$$HTN$$C6$$" />
                      </Action>
                      <Action ActionType="1" Name="TAD" Key="Condition18">
                        <ActionProperty Name="IfConnectionLogic" Value="1" />
                        <Checks>
                          <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                            <CheckProperty Name="IfCheckRuleID" Value="8" />
                          </Check>
                        </Checks>
                        <TrueBranch>
                          <Action ActionType="3" Name="Action5" Key="Action38">
                            <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$Family Hx of CVD$$C5$$HTN$$C5$$Tobacco\Drug\Alcohol$$C6$$" />
                          </Action>
                          <Action ActionType="1" Name="DM" Key="Condition19">
                            <ActionProperty Name="IfConnectionLogic" Value="1" />
                            <Checks>
                              <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                                <CheckProperty Name="IfCheckRuleID" Value="9" />
                              </Check>
                            </Checks>
                            <TrueBranch>
                              <Action ActionType="3" Name="Action6" Key="Action20">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$Family Hx of CVD$$C5$$HTN$$C5$$Tobacco\Drug\Alcohol$$C5$$DM$$C6$$" />
                              </Action>
                            </TrueBranch>
                            <FalseBranch>
                              <Action ActionType="3" Name="Action6" Key="Action19">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$Family Hx of CVD$$C5$$HTN$$C5$$Tobacco\Drug\Alcohol$$C6$$" />
                              </Action>
                            </FalseBranch>
                          </Action>
                        </TrueBranch>
                        <FalseBranch>
                          <Action ActionType="3" Name="Action5" Key="Action40">
                            <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$Family Hx of CVD$$C5$$HTN$$C6$$" />
                          </Action>
                          <Action ActionType="1" Name="DM" Key="Condition20">
                            <ActionProperty Name="IfConnectionLogic" Value="1" />
                            <Checks>
                              <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                                <CheckProperty Name="IfCheckRuleID" Value="10" />
                              </Check>
                            </Checks>
                            <TrueBranch>
                              <Action ActionType="3" Name="Action6" Key="Action21">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$Family Hx of CVD$$C5$$HTN$$C5$$DM$$C6$$" />
                              </Action>
                            </TrueBranch>
                            <FalseBranch>
                              <Action ActionType="3" Name="Action6" Key="Action23">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$Family Hx of CVD$$C5$$HTN$$C6$$" />
                              </Action>
                            </FalseBranch>
                          </Action>
                        </FalseBranch>
                      </Action>
                    </FalseBranch>
                  </Action>
                </TrueBranch>
                <FalseBranch>
                  <Action ActionType="3" Name="Action3" Key="Action42">
                    <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                    <ActionProperty Name="SetValueOptions" Value="1" />
                    <ActionProperty Name="SetValueWhich" Value="1" />
                    <ActionProperty Name="SetValueComponentID" Value="Screening" />
                    <ActionProperty Name="SetValueComponentValue" Value="Family Hx of CVD$$C5$$Obesity$$C6$$" />
                  </Action>
                  <Action ActionType="1" Name="HLD" Key="Condition21">
                    <ActionProperty Name="IfConnectionLogic" Value="1" />
                    <Checks>
                      <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                        <CheckProperty Name="IfCheckRuleID" Value="11" />
                      </Check>
                    </Checks>
                    <TrueBranch>
                      <Action ActionType="3" Name="Action4" Key="Action136">
                        <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                        <ActionProperty Name="SetValueOptions" Value="1" />
                        <ActionProperty Name="SetValueWhich" Value="1" />
                        <ActionProperty Name="SetValueComponentID" Value="Screening" />
                        <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$Family Hx of CVD$$C5$$HLD$$C6$$" />
                      </Action>
                      <Action ActionType="1" Name="TAD" Key="Condition22">
                        <ActionProperty Name="IfConnectionLogic" Value="1" />
                        <Checks>
                          <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                            <CheckProperty Name="IfCheckRuleID" Value="12" />
                          </Check>
                        </Checks>
                        <TrueBranch>
                          <Action ActionType="3" Name="Action5" Key="Action41">
                            <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$Family Hx of CVD$$C5$$HLD$$C5$$Tobacco\Drug\Alcohol$$C6$$" />
                          </Action>
                          <Action ActionType="1" Name="DM" Key="Condition23">
                            <ActionProperty Name="IfConnectionLogic" Value="1" />
                            <Checks>
                              <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                                <CheckProperty Name="IfCheckRuleID" Value="13" />
                              </Check>
                            </Checks>
                            <TrueBranch>
                              <Action ActionType="3" Name="Action6" Key="Action25">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$Family Hx of CVD$$C5$$HLD$$C5$$Tobacco\Drug\Alcohol$$C5$$DM$$C6$$" />
                              </Action>
                            </TrueBranch>
                            <FalseBranch>
                              <Action ActionType="3" Name="Action6" Key="Action26">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$Family Hx of CVD$$C5$$HLD$$C5$$Tobacco\Drug\Alcohol$$C6$$" />
                              </Action>
                            </FalseBranch>
                          </Action>
                        </TrueBranch>
                        <FalseBranch>
                          <Action ActionType="3" Name="Action5" Key="Action44">
                            <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$Family Hx of CVD$$C5$$HLD$$C6$$" />
                          </Action>
                          <Action ActionType="1" Name="DM" Key="Condition24">
                            <ActionProperty Name="IfConnectionLogic" Value="1" />
                            <Checks>
                              <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                                <CheckProperty Name="IfCheckRuleID" Value="14" />
                              </Check>
                            </Checks>
                            <TrueBranch>
                              <Action ActionType="3" Name="Action6" Key="Action29">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$Family Hx of CVD$$C5$$HLD$$C5$$DM$$C6$$" />
                              </Action>
                            </TrueBranch>
                            <FalseBranch>
                              <Action ActionType="3" Name="Action6" Key="Action30">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$Family Hx of CVD$$C5$$HLD$$C6$$" />
                              </Action>
                            </FalseBranch>
                          </Action>
                        </FalseBranch>
                      </Action>
                    </TrueBranch>
                    <FalseBranch>
                      <Action ActionType="3" Name="Action4" Key="Action27">
                        <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                        <ActionProperty Name="SetValueOptions" Value="1" />
                        <ActionProperty Name="SetValueWhich" Value="1" />
                        <ActionProperty Name="SetValueComponentID" Value="Screening" />
                        <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$Family Hx of CVD$$C6$$" />
                      </Action>
                      <Action ActionType="1" Name="TAD" Key="Condition25">
                        <ActionProperty Name="IfConnectionLogic" Value="1" />
                        <Checks>
                          <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                            <CheckProperty Name="IfCheckRuleID" Value="15" />
                          </Check>
                        </Checks>
                        <TrueBranch>
                          <Action ActionType="3" Name="Action5" Key="Action45">
                            <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$Family Hx of CVD$$C5$$Tobacco\Drug\Alcohol$$C6$$" />
                          </Action>
                          <Action ActionType="1" Name="DM" Key="Condition26">
                            <ActionProperty Name="IfConnectionLogic" Value="1" />
                            <Checks>
                              <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                                <CheckProperty Name="IfCheckRuleID" Value="16" />
                              </Check>
                            </Checks>
                            <TrueBranch>
                              <Action ActionType="3" Name="Action6" Key="Action73">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$Family Hx of CVD$$C5$$Tobacco\Drug\Alcohol$$C5$$DM$$C6$$" />
                              </Action>
                            </TrueBranch>
                            <FalseBranch>
                              <Action ActionType="3" Name="Action6" Key="Action74">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$Family Hx of CVD$$C5$$Tobacco\Drug\Alcohol$$C6$$" />
                              </Action>
                            </FalseBranch>
                          </Action>
                        </TrueBranch>
                        <FalseBranch>
                          <Action ActionType="3" Name="Action5" Key="Action47">
                            <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$Family Hx of CVD$$C6$$" />
                          </Action>
                          <Action ActionType="1" Name="DM" Key="Condition27">
                            <ActionProperty Name="IfConnectionLogic" Value="1" />
                            <Checks>
                              <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                                <CheckProperty Name="IfCheckRuleID" Value="17" />
                              </Check>
                            </Checks>
                            <TrueBranch>
                              <Action ActionType="3" Name="Action6" Key="Action75">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$Family Hx of CVD$$C5$$DM$$C6$$" />
                              </Action>
                            </TrueBranch>
                            <FalseBranch>
                              <Action ActionType="3" Name="Action6" Key="Action76">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$Family Hx of CVD$$C6$$" />
                              </Action>
                            </FalseBranch>
                          </Action>
                        </FalseBranch>
                      </Action>
                    </FalseBranch>
                  </Action>
                </FalseBranch>
              </Action>
            </TrueBranch>
            <FalseBranch>
              <Action ActionType="3" Name="Action2" Key="Action31">
                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                <ActionProperty Name="SetValueOptions" Value="1" />
                <ActionProperty Name="SetValueWhich" Value="1" />
                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C6$$" />
              </Action>
              <Action ActionType="1" Name="HTN" Key="Condition28">
                <ActionProperty Name="IfConnectionLogic" Value="1" />
                <Checks>
                  <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                    <CheckProperty Name="IfCheckRuleID" Value="18" />
                  </Check>
                </Checks>
                <TrueBranch>
                  <Action ActionType="3" Name="Action3" Key="Action51">
                    <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                    <ActionProperty Name="SetValueOptions" Value="1" />
                    <ActionProperty Name="SetValueWhich" Value="1" />
                    <ActionProperty Name="SetValueComponentID" Value="Screening" />
                    <ActionProperty Name="SetValueComponentValue" Value="HTN$$C5$$Obesity$$C6$$" />
                  </Action>
                  <Action ActionType="1" Name="HLD" Key="Condition29">
                    <ActionProperty Name="IfConnectionLogic" Value="1" />
                    <Checks>
                      <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                        <CheckProperty Name="IfCheckRuleID" Value="19" />
                      </Check>
                    </Checks>
                    <TrueBranch>
                      <Action ActionType="3" Name="Action4" Key="Action35">
                        <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                        <ActionProperty Name="SetValueOptions" Value="1" />
                        <ActionProperty Name="SetValueWhich" Value="1" />
                        <ActionProperty Name="SetValueComponentID" Value="Screening" />
                        <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$HTN$$C5$$HLD$$C6$$" />
                      </Action>
                      <Action ActionType="1" Name="TAD" Key="Condition30">
                        <ActionProperty Name="IfConnectionLogic" Value="1" />
                        <Checks>
                          <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                            <CheckProperty Name="IfCheckRuleID" Value="20" />
                          </Check>
                        </Checks>
                        <TrueBranch>
                          <Action ActionType="3" Name="Action5" Key="Action48">
                            <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$HTN$$C5$$HLD$$C5$$Tobacco\Drug\Alcohol$$C6$$" />
                          </Action>
                          <Action ActionType="1" Name="DM" Key="Condition31">
                            <ActionProperty Name="IfConnectionLogic" Value="1" />
                            <Checks>
                              <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                                <CheckProperty Name="IfCheckRuleID" Value="21" />
                              </Check>
                            </Checks>
                            <TrueBranch>
                              <Action ActionType="3" Name="Action6" Key="Action97">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$HTN$$C5$$HLD$$C5$$Tobacco\Drug\Alcohol$$C5$$DM$$C6$$" />
                              </Action>
                            </TrueBranch>
                            <FalseBranch>
                              <Action ActionType="3" Name="Action6" Key="Action98">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$HTN$$C5$$HLD$$C5$$Tobacco\Drug\Alcohol$$C6$$" />
                              </Action>
                            </FalseBranch>
                          </Action>
                        </TrueBranch>
                        <FalseBranch>
                          <Action ActionType="3" Name="Action5" Key="Action24">
                            <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$HTN$$C5$$HLD$$C6$$" />
                          </Action>
                          <Action ActionType="1" Name="DM" Key="Condition32">
                            <ActionProperty Name="IfConnectionLogic" Value="1" />
                            <Checks>
                              <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                                <CheckProperty Name="IfCheckRuleID" Value="22" />
                              </Check>
                            </Checks>
                            <TrueBranch>
                              <Action ActionType="3" Name="Action6" Key="Action32">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$HTN$$C5$$HLD$$C5$$DM$$C6$$" />
                              </Action>
                            </TrueBranch>
                            <FalseBranch>
                              <Action ActionType="3" Name="Action6" Key="Action33">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$HTN$$C5$$HLD$$C6$$" />
                              </Action>
                            </FalseBranch>
                          </Action>
                        </FalseBranch>
                      </Action>
                    </TrueBranch>
                    <FalseBranch>
                      <Action ActionType="3" Name="Action4" Key="Action39">
                        <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                        <ActionProperty Name="SetValueOptions" Value="1" />
                        <ActionProperty Name="SetValueWhich" Value="1" />
                        <ActionProperty Name="SetValueComponentID" Value="Screening" />
                        <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$HTN$$C6$$" />
                      </Action>
                      <Action ActionType="1" Name="TAD" Key="Condition33">
                        <ActionProperty Name="IfConnectionLogic" Value="1" />
                        <Checks>
                          <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                            <CheckProperty Name="IfCheckRuleID" Value="23" />
                          </Check>
                        </Checks>
                        <TrueBranch>
                          <Action ActionType="3" Name="Action5" Key="Action53">
                            <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$HTN$$C5$$Tobacco\Drug\Alcohol$$C6$$" />
                          </Action>
                          <Action ActionType="1" Name="DM" Key="Condition34">
                            <ActionProperty Name="IfConnectionLogic" Value="1" />
                            <Checks>
                              <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                                <CheckProperty Name="IfCheckRuleID" Value="24" />
                              </Check>
                            </Checks>
                            <TrueBranch>
                              <Action ActionType="3" Name="Action6" Key="Action99">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$HTN$$C5$$Tobacco\Drug\Alcohol$$C5$$DM$$C6$$" />
                              </Action>
                            </TrueBranch>
                            <FalseBranch>
                              <Action ActionType="3" Name="Action6" Key="Action100">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$HTN$$C5$$Tobacco\Drug\Alcohol$$C6$$" />
                              </Action>
                            </FalseBranch>
                          </Action>
                        </TrueBranch>
                        <FalseBranch>
                          <Action ActionType="3" Name="Action5" Key="Action28">
                            <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$HTN$$C6$$" />
                          </Action>
                          <Action ActionType="1" Name="DM" Key="Condition35">
                            <ActionProperty Name="IfConnectionLogic" Value="1" />
                            <Checks>
                              <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                                <CheckProperty Name="IfCheckRuleID" Value="25" />
                              </Check>
                            </Checks>
                            <TrueBranch>
                              <Action ActionType="3" Name="Action6" Key="Action101">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$HTN$$C5$$DM$$C6$$" />
                              </Action>
                            </TrueBranch>
                            <FalseBranch>
                              <Action ActionType="3" Name="Action6" Key="Action102">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$HTN$$C6$$" />
                              </Action>
                            </FalseBranch>
                          </Action>
                        </FalseBranch>
                      </Action>
                    </FalseBranch>
                  </Action>
                </TrueBranch>
                <FalseBranch>
                  <Action ActionType="3" Name="Action3" Key="Action58">
                    <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                    <ActionProperty Name="SetValueOptions" Value="1" />
                    <ActionProperty Name="SetValueWhich" Value="1" />
                    <ActionProperty Name="SetValueComponentID" Value="Screening" />
                    <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C6$$" />
                  </Action>
                  <Action ActionType="1" Name="HLD" Key="Condition36">
                    <ActionProperty Name="IfConnectionLogic" Value="1" />
                    <Checks>
                      <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                        <CheckProperty Name="IfCheckRuleID" Value="26" />
                      </Check>
                    </Checks>
                    <TrueBranch>
                      <Action ActionType="3" Name="Action4" Key="Action132">
                        <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                        <ActionProperty Name="SetValueOptions" Value="1" />
                        <ActionProperty Name="SetValueWhich" Value="1" />
                        <ActionProperty Name="SetValueComponentID" Value="Screening" />
                        <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$HLD$$C6$$" />
                      </Action>
                      <Action ActionType="1" Name="TAD" Key="Condition37">
                        <ActionProperty Name="IfConnectionLogic" Value="1" />
                        <Checks>
                          <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                            <CheckProperty Name="IfCheckRuleID" Value="27" />
                          </Check>
                        </Checks>
                        <TrueBranch>
                          <Action ActionType="3" Name="Action5" Key="Action54">
                            <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$HLD$$C5$$Tobacco\Drug\Alcohol$$C6$$" />
                          </Action>
                          <Action ActionType="1" Name="DM" Key="Condition66">
                            <ActionProperty Name="IfConnectionLogic" Value="1" />
                            <Checks>
                              <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                                <CheckProperty Name="IfCheckRuleID" Value="28" />
                              </Check>
                            </Checks>
                            <TrueBranch>
                              <Action ActionType="3" Name="Action6" Key="Action103">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$HLD$$C5$$Tobacco\Drug\Alcohol$$C5$$DM$$C6$$" />
                              </Action>
                            </TrueBranch>
                            <FalseBranch>
                              <Action ActionType="3" Name="Action6" Key="Action104">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$HLD$$C5$$Tobacco\Drug\Alcohol$$C6$$" />
                              </Action>
                            </FalseBranch>
                          </Action>
                        </TrueBranch>
                        <FalseBranch>
                          <Action ActionType="3" Name="Action5" Key="Action56">
                            <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$HLD$$C6$$" />
                          </Action>
                          <Action ActionType="1" Name="DM" Key="Condition67">
                            <ActionProperty Name="IfConnectionLogic" Value="1" />
                            <Checks>
                              <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                                <CheckProperty Name="IfCheckRuleID" Value="29" />
                              </Check>
                            </Checks>
                            <TrueBranch>
                              <Action ActionType="3" Name="Action6" Key="Action105">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$DM$$C5$$HTN$$C6$$" />
                              </Action>
                            </TrueBranch>
                            <FalseBranch>
                              <Action ActionType="3" Name="Action6" Key="Action106">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$HLD$$C6$$" />
                              </Action>
                            </FalseBranch>
                          </Action>
                        </FalseBranch>
                      </Action>
                    </TrueBranch>
                    <FalseBranch>
                      <Action ActionType="3" Name="Action4" Key="Action43">
                        <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                        <ActionProperty Name="SetValueOptions" Value="1" />
                        <ActionProperty Name="SetValueWhich" Value="1" />
                        <ActionProperty Name="SetValueComponentID" Value="Screening" />
                        <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C6$$" />
                      </Action>
                      <Action ActionType="1" Name="TAD" Key="Condition68">
                        <ActionProperty Name="IfConnectionLogic" Value="1" />
                        <Checks>
                          <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                            <CheckProperty Name="IfCheckRuleID" Value="30" />
                          </Check>
                        </Checks>
                        <TrueBranch>
                          <Action ActionType="3" Name="Action5" Key="Action60">
                            <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$Tobacco\Drug\Alcohol$$C6$$" />
                          </Action>
                          <Action ActionType="1" Name="DM" Key="Condition69">
                            <ActionProperty Name="IfConnectionLogic" Value="1" />
                            <Checks>
                              <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                                <CheckProperty Name="IfCheckRuleID" Value="31" />
                              </Check>
                            </Checks>
                            <TrueBranch>
                              <Action ActionType="3" Name="Action6" Key="Action107">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$Tobacco\Drug\Alcohol$$C5$$DM$$C6$$" />
                              </Action>
                            </TrueBranch>
                            <FalseBranch>
                              <Action ActionType="3" Name="Action6" Key="Action108">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$Tobacco\Drug\Alcohol$$C6$$" />
                              </Action>
                            </FalseBranch>
                          </Action>
                        </TrueBranch>
                        <FalseBranch>
                          <Action ActionType="3" Name="Action5" Key="Action49">
                            <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C6$$" />
                          </Action>
                          <Action ActionType="1" Name="DM" Key="Condition70">
                            <ActionProperty Name="IfConnectionLogic" Value="1" />
                            <Checks>
                              <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                                <CheckProperty Name="IfCheckRuleID" Value="32" />
                              </Check>
                            </Checks>
                            <TrueBranch>
                              <Action ActionType="3" Name="Action6" Key="Action109">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C5$$DM$$C6$$" />
                              </Action>
                            </TrueBranch>
                            <FalseBranch>
                              <Action ActionType="3" Name="Action6" Key="Action110">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Obesity$$C6$$" />
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
        </TrueBranch>
        <FalseBranch>
          <Action ActionType="3" Name="Action1" Key="Action138">
            <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
            <ActionProperty Name="SetValueOptions" Value="1" />
            <ActionProperty Name="SetValueWhich" Value="1" />
            <ActionProperty Name="SetValueComponentID" Value="Screening" />
            <ActionProperty Name="SetValueComponentValue" Value="$$C6$$" />
          </Action>
          <Action ActionType="1" Name="FamHx" Key="Condition71">
            <ActionProperty Name="IfConnectionLogic" Value="1" />
            <Checks>
              <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                <CheckProperty Name="IfCheckRuleID" Value="33" />
              </Check>
            </Checks>
            <TrueBranch>
              <Action ActionType="3" Name="Action2" Key="Action36">
                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                <ActionProperty Name="SetValueOptions" Value="1" />
                <ActionProperty Name="SetValueWhich" Value="1" />
                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                <ActionProperty Name="SetValueComponentValue" Value="Family Hx of CVD$$C6$$" />
              </Action>
              <Action ActionType="1" Name="HTN" Key="Condition72">
                <ActionProperty Name="IfConnectionLogic" Value="1" />
                <Checks>
                  <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                    <CheckProperty Name="IfCheckRuleID" Value="34" />
                  </Check>
                </Checks>
                <TrueBranch>
                  <Action ActionType="3" Name="Action3" Key="Action34">
                    <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                    <ActionProperty Name="SetValueOptions" Value="1" />
                    <ActionProperty Name="SetValueWhich" Value="1" />
                    <ActionProperty Name="SetValueComponentID" Value="Screening" />
                    <ActionProperty Name="SetValueComponentValue" Value="Family Hx of CVD$$C5$$HTN$$C6$$" />
                  </Action>
                  <Action ActionType="1" Name="HLD" Key="Condition73">
                    <ActionProperty Name="IfConnectionLogic" Value="1" />
                    <Checks>
                      <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                        <CheckProperty Name="IfCheckRuleID" Value="35" />
                      </Check>
                    </Checks>
                    <TrueBranch>
                      <Action ActionType="3" Name="Action4" Key="Action46">
                        <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                        <ActionProperty Name="SetValueOptions" Value="1" />
                        <ActionProperty Name="SetValueWhich" Value="1" />
                        <ActionProperty Name="SetValueComponentID" Value="Screening" />
                        <ActionProperty Name="SetValueComponentValue" Value="Family Hx of CVD$$C5$$HTN$$C5$$HLD$$C6$$" />
                      </Action>
                      <Action ActionType="1" Name="TAD" Key="Condition74">
                        <ActionProperty Name="IfConnectionLogic" Value="1" />
                        <Checks>
                          <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                            <CheckProperty Name="IfCheckRuleID" Value="36" />
                          </Check>
                        </Checks>
                        <TrueBranch>
                          <Action ActionType="3" Name="Action5" Key="Action61">
                            <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueComponentValue" Value="Family Hx of CVD$$C5$$HTN$$C5$$HLD$$C5$$Tobacco\Drug\Alcohol$$C6$$" />
                          </Action>
                          <Action ActionType="1" Name="DM" Key="Condition75">
                            <ActionProperty Name="IfConnectionLogic" Value="1" />
                            <Checks>
                              <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                                <CheckProperty Name="IfCheckRuleID" Value="37" />
                              </Check>
                            </Checks>
                            <TrueBranch>
                              <Action ActionType="3" Name="Action6" Key="Action111">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Family Hx of CVD$$C5$$HTN$$C5$$HLD$$C5$$Tobacco\Drug\Alcohol$$C5$$DM$$C6$$" />
                              </Action>
                            </TrueBranch>
                            <FalseBranch>
                              <Action ActionType="3" Name="Action6" Key="Action112">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Family Hx of CVD$$C5$$HTN$$C5$$HLD$$C5$$Tobacco\Drug\Alcohol$$C6$$" />
                              </Action>
                            </FalseBranch>
                          </Action>
                        </TrueBranch>
                        <FalseBranch>
                          <Action ActionType="3" Name="Action5" Key="Action63">
                            <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueComponentValue" Value="Family Hx of CVD$$C5$$HTN$$C5$$HLD$$C6$$" />
                          </Action>
                          <Action ActionType="1" Name="DM" Key="Condition76">
                            <ActionProperty Name="IfConnectionLogic" Value="1" />
                            <Checks>
                              <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                                <CheckProperty Name="IfCheckRuleID" Value="38" />
                              </Check>
                            </Checks>
                            <TrueBranch>
                              <Action ActionType="3" Name="Action6" Key="Action113">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Family Hx of CVD$$C5$$HTN$$C5$$HLD$$C5$$DM$$C6$$" />
                              </Action>
                            </TrueBranch>
                            <FalseBranch>
                              <Action ActionType="3" Name="Action6" Key="Action114">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Family Hx of CVD$$C5$$HTN$$C5$$HLD$$C6$$" />
                              </Action>
                            </FalseBranch>
                          </Action>
                        </FalseBranch>
                      </Action>
                    </TrueBranch>
                    <FalseBranch>
                      <Action ActionType="3" Name="Action4" Key="Action70">
                        <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                        <ActionProperty Name="SetValueOptions" Value="1" />
                        <ActionProperty Name="SetValueWhich" Value="1" />
                        <ActionProperty Name="SetValueComponentID" Value="Screening" />
                        <ActionProperty Name="SetValueComponentValue" Value="Family Hx of CVD$$C5$$HTN$$C6$$" />
                      </Action>
                      <Action ActionType="1" Name="TAD" Key="Condition77">
                        <ActionProperty Name="IfConnectionLogic" Value="1" />
                        <Checks>
                          <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                            <CheckProperty Name="IfCheckRuleID" Value="39" />
                          </Check>
                        </Checks>
                        <TrueBranch>
                          <Action ActionType="3" Name="Action5" Key="Action64">
                            <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueComponentValue" Value="Family Hx of CVD$$C5$$HTN$$C5$$Tobacco\Drug\Alcohol$$C6$$" />
                          </Action>
                          <Action ActionType="1" Name="DM" Key="Condition78">
                            <ActionProperty Name="IfConnectionLogic" Value="1" />
                            <Checks>
                              <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                                <CheckProperty Name="IfCheckRuleID" Value="40" />
                              </Check>
                            </Checks>
                            <TrueBranch>
                              <Action ActionType="3" Name="Action6" Key="Action115">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Family Hx of CVD$$C5$$Tobacco\Drug\Alcohol$$C5$$DM$$C5$$HTN$$C6$$" />
                              </Action>
                            </TrueBranch>
                            <FalseBranch>
                              <Action ActionType="3" Name="Action6" Key="Action116">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Family Hx of CVD$$C5$$HTN$$C5$$Tobacco\Drug\Alcohol$$C6$$" />
                              </Action>
                            </FalseBranch>
                          </Action>
                        </TrueBranch>
                        <FalseBranch>
                          <Action ActionType="3" Name="Action5" Key="Action68">
                            <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueComponentValue" Value="Family Hx of CVD$$C5$$HTN$$C6$$" />
                          </Action>
                          <Action ActionType="1" Name="DM" Key="Condition79">
                            <ActionProperty Name="IfConnectionLogic" Value="1" />
                            <Checks>
                              <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                                <CheckProperty Name="IfCheckRuleID" Value="41" />
                              </Check>
                            </Checks>
                            <TrueBranch>
                              <Action ActionType="3" Name="Action6" Key="Action117">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Family Hx of CVD$$C5$$HTN$$C5$$DM$$C6$$" />
                              </Action>
                            </TrueBranch>
                            <FalseBranch>
                              <Action ActionType="3" Name="Action6" Key="Action118">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Family Hx of CVD$$C5$$HTN$$C6$$" />
                              </Action>
                            </FalseBranch>
                          </Action>
                        </FalseBranch>
                      </Action>
                    </FalseBranch>
                  </Action>
                </TrueBranch>
                <FalseBranch>
                  <Action ActionType="3" Name="Action3" Key="Action50">
                    <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                    <ActionProperty Name="SetValueOptions" Value="1" />
                    <ActionProperty Name="SetValueWhich" Value="1" />
                    <ActionProperty Name="SetValueComponentID" Value="Screening" />
                    <ActionProperty Name="SetValueComponentValue" Value="Family Hx of CVD$$C6$$" />
                  </Action>
                  <Action ActionType="1" Name="HLD" Key="Condition80">
                    <ActionProperty Name="IfConnectionLogic" Value="1" />
                    <Checks>
                      <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                        <CheckProperty Name="IfCheckRuleID" Value="42" />
                      </Check>
                    </Checks>
                    <TrueBranch>
                      <Action ActionType="3" Name="Action4" Key="Action52">
                        <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                        <ActionProperty Name="SetValueOptions" Value="1" />
                        <ActionProperty Name="SetValueWhich" Value="1" />
                        <ActionProperty Name="SetValueComponentID" Value="Screening" />
                        <ActionProperty Name="SetValueComponentValue" Value="Family Hx of CVD$$C5$$HLD$$C6$$" />
                      </Action>
                      <Action ActionType="1" Name="TAD" Key="Condition81">
                        <ActionProperty Name="IfConnectionLogic" Value="1" />
                        <Checks>
                          <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                            <CheckProperty Name="IfCheckRuleID" Value="43" />
                          </Check>
                        </Checks>
                        <TrueBranch>
                          <Action ActionType="3" Name="Action5" Key="Action69">
                            <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueComponentValue" Value="Family Hx of CVD$$C5$$HLD$$C5$$Tobacco\Drug\Alcohol$$C6$$" />
                          </Action>
                          <Action ActionType="1" Name="DM" Key="Condition82">
                            <ActionProperty Name="IfConnectionLogic" Value="1" />
                            <Checks>
                              <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                                <CheckProperty Name="IfCheckRuleID" Value="44" />
                              </Check>
                            </Checks>
                            <TrueBranch>
                              <Action ActionType="3" Name="Action6" Key="Action119">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Family Hx of CVD$$C5$$Tobacco\Drug\Alcohol$$C5$$DM$$C5$$HLD$$C6$$" />
                              </Action>
                            </TrueBranch>
                            <FalseBranch>
                              <Action ActionType="3" Name="Action6" Key="Action120">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Family Hx of CVD$$C5$$HLD$$C5$$Tobacco\Drug\Alcohol$$C6$$" />
                              </Action>
                            </FalseBranch>
                          </Action>
                        </TrueBranch>
                        <FalseBranch>
                          <Action ActionType="3" Name="Action5" Key="Action71">
                            <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueComponentValue" Value="Family Hx of CVD$$C5$$HLD$$C6$$" />
                          </Action>
                          <Action ActionType="1" Name="DM" Key="Condition83">
                            <ActionProperty Name="IfConnectionLogic" Value="1" />
                            <Checks>
                              <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                                <CheckProperty Name="IfCheckRuleID" Value="45" />
                              </Check>
                            </Checks>
                            <TrueBranch>
                              <Action ActionType="3" Name="Action6" Key="Action121">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Family Hx of CVD$$C5$$DM$$C5$$HLD$$C6$$" />
                              </Action>
                            </TrueBranch>
                            <FalseBranch>
                              <Action ActionType="3" Name="Action6" Key="Action122">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Family Hx of CVD$$C5$$HLD$$C6$$" />
                              </Action>
                            </FalseBranch>
                          </Action>
                        </FalseBranch>
                      </Action>
                    </TrueBranch>
                    <FalseBranch>
                      <Action ActionType="3" Name="Action4" Key="Action55">
                        <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                        <ActionProperty Name="SetValueOptions" Value="1" />
                        <ActionProperty Name="SetValueWhich" Value="1" />
                        <ActionProperty Name="SetValueComponentID" Value="Screening" />
                        <ActionProperty Name="SetValueComponentValue" Value="Family Hx of CVD$$C6$$" />
                      </Action>
                      <Action ActionType="1" Name="TAD" Key="Condition84">
                        <ActionProperty Name="IfConnectionLogic" Value="1" />
                        <Checks>
                          <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                            <CheckProperty Name="IfCheckRuleID" Value="46" />
                          </Check>
                        </Checks>
                        <TrueBranch>
                          <Action ActionType="3" Name="Action5" Key="Action130">
                            <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueComponentValue" Value="Family Hx of CVD$$C5$$Tobacco\Drug\Alcohol$$C6$$" />
                          </Action>
                          <Action ActionType="1" Name="DM" Key="Condition85">
                            <ActionProperty Name="IfConnectionLogic" Value="1" />
                            <Checks>
                              <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                                <CheckProperty Name="IfCheckRuleID" Value="47" />
                              </Check>
                            </Checks>
                            <TrueBranch>
                              <Action ActionType="3" Name="Action6" Key="Action165">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Family Hx of CVD$$C5$$Tobacco\Drug\Alcohol$$C5$$DM$$C6$$" />
                              </Action>
                            </TrueBranch>
                            <FalseBranch>
                              <Action ActionType="3" Name="Action6" Key="Action95">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Family Hx of CVD$$C5$$Tobacco\Drug\Alcohol$$C6$$" />
                              </Action>
                            </FalseBranch>
                          </Action>
                        </TrueBranch>
                        <FalseBranch>
                          <Action ActionType="3" Name="Action5" Key="Action129">
                            <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueComponentValue" Value="Family Hx of CVD$$C6$$" />
                          </Action>
                          <Action ActionType="1" Name="DM" Key="Condition86">
                            <ActionProperty Name="IfConnectionLogic" Value="1" />
                            <Checks>
                              <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                                <CheckProperty Name="IfCheckRuleID" Value="48" />
                              </Check>
                            </Checks>
                            <TrueBranch>
                              <Action ActionType="3" Name="Action6" Key="Action94">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Family Hx of CVD$$C5$$DM$$C6$$" />
                              </Action>
                            </TrueBranch>
                            <FalseBranch>
                              <Action ActionType="3" Name="Action6" Key="Action93">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Family Hx of CVD$$C6$$" />
                              </Action>
                            </FalseBranch>
                          </Action>
                        </FalseBranch>
                      </Action>
                    </FalseBranch>
                  </Action>
                </FalseBranch>
              </Action>
            </TrueBranch>
            <FalseBranch>
              <Action ActionType="3" Name="Action2" Key="Action133">
                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                <ActionProperty Name="SetValueOptions" Value="1" />
                <ActionProperty Name="SetValueWhich" Value="1" />
                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                <ActionProperty Name="SetValueComponentValue" Value="$$C6$$" />
              </Action>
              <Action ActionType="1" Name="HTN" Key="Condition87">
                <ActionProperty Name="IfConnectionLogic" Value="1" />
                <Checks>
                  <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                    <CheckProperty Name="IfCheckRuleID" Value="49" />
                  </Check>
                </Checks>
                <TrueBranch>
                  <Action ActionType="3" Name="Action3" Key="Action171">
                    <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                    <ActionProperty Name="SetValueOptions" Value="1" />
                    <ActionProperty Name="SetValueWhich" Value="1" />
                    <ActionProperty Name="SetValueComponentID" Value="Screening" />
                    <ActionProperty Name="SetValueComponentValue" Value="$$C6$$" />
                  </Action>
                  <Action ActionType="1" Name="HLD" Key="Condition88">
                    <ActionProperty Name="IfConnectionLogic" Value="1" />
                    <Checks>
                      <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                        <CheckProperty Name="IfCheckRuleID" Value="50" />
                      </Check>
                    </Checks>
                    <TrueBranch>
                      <Action ActionType="3" Name="Action4" Key="Action57">
                        <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                        <ActionProperty Name="SetValueOptions" Value="1" />
                        <ActionProperty Name="SetValueWhich" Value="1" />
                        <ActionProperty Name="SetValueComponentID" Value="Screening" />
                        <ActionProperty Name="SetValueComponentValue" Value="HTN$$C5$$HLD$$C6$$" />
                      </Action>
                      <Action ActionType="1" Name="TAD" Key="Condition89">
                        <ActionProperty Name="IfConnectionLogic" Value="1" />
                        <Checks>
                          <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                            <CheckProperty Name="IfCheckRuleID" Value="51" />
                          </Check>
                        </Checks>
                        <TrueBranch>
                          <Action ActionType="3" Name="Action5" Key="Action128">
                            <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueComponentValue" Value="HTN$$C5$$HLD$$C5$$Tobacco\Drug\Alcohol$$C6$$" />
                          </Action>
                          <Action ActionType="1" Name="DM" Key="Condition90">
                            <ActionProperty Name="IfConnectionLogic" Value="1" />
                            <Checks>
                              <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                                <CheckProperty Name="IfCheckRuleID" Value="52" />
                              </Check>
                            </Checks>
                            <TrueBranch>
                              <Action ActionType="3" Name="Action6" Key="Action92">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="HTN$$C5$$HLD$$C5$$Tobacco\Drug\Alcohol$$C5$$DM$$C6$$" />
                              </Action>
                            </TrueBranch>
                            <FalseBranch>
                              <Action ActionType="3" Name="Action6" Key="Action91">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="HTN$$C5$$HLD$$C5$$Tobacco\Drug\Alcohol$$C6$$" />
                              </Action>
                            </FalseBranch>
                          </Action>
                        </TrueBranch>
                        <FalseBranch>
                          <Action ActionType="3" Name="Action5" Key="Action127">
                            <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueComponentValue" Value="HTN$$C5$$HLD$$C6$$" />
                          </Action>
                          <Action ActionType="1" Name="DM" Key="Condition91">
                            <ActionProperty Name="IfConnectionLogic" Value="1" />
                            <Checks>
                              <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                                <CheckProperty Name="IfCheckRuleID" Value="53" />
                              </Check>
                            </Checks>
                            <TrueBranch>
                              <Action ActionType="3" Name="Action6" Key="Action90">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="HTN$$C5$$HLD$$C5$$DM$$C6$$" />
                              </Action>
                            </TrueBranch>
                            <FalseBranch>
                              <Action ActionType="3" Name="Action6" Key="Action89">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="HTN$$C5$$HLD$$C6$$" />
                              </Action>
                            </FalseBranch>
                          </Action>
                        </FalseBranch>
                      </Action>
                    </TrueBranch>
                    <FalseBranch>
                      <Action ActionType="3" Name="Action4" Key="Action59">
                        <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                        <ActionProperty Name="SetValueOptions" Value="1" />
                        <ActionProperty Name="SetValueWhich" Value="1" />
                        <ActionProperty Name="SetValueComponentID" Value="Screening" />
                        <ActionProperty Name="SetValueComponentValue" Value="HTN$$C6$$" />
                      </Action>
                      <Action ActionType="1" Name="TAD" Key="Condition92">
                        <ActionProperty Name="IfConnectionLogic" Value="1" />
                        <Checks>
                          <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                            <CheckProperty Name="IfCheckRuleID" Value="54" />
                          </Check>
                        </Checks>
                        <TrueBranch>
                          <Action ActionType="3" Name="Action5" Key="Action125">
                            <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueComponentValue" Value="HTN$$C5$$Tobacco\Drug\Alcohol$$C6$$" />
                          </Action>
                          <Action ActionType="1" Name="DM" Key="Condition93">
                            <ActionProperty Name="IfConnectionLogic" Value="1" />
                            <Checks>
                              <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                                <CheckProperty Name="IfCheckRuleID" Value="55" />
                              </Check>
                            </Checks>
                            <TrueBranch>
                              <Action ActionType="3" Name="Action6" Key="Action88">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="HTN$$C5$$Tobacco\Drug\Alcohol$$C5$$DM$$C6$$" />
                              </Action>
                            </TrueBranch>
                            <FalseBranch>
                              <Action ActionType="3" Name="Action6" Key="Action87">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="HTN$$C5$$Tobacco\Drug\Alcohol$$C6$$" />
                              </Action>
                            </FalseBranch>
                          </Action>
                        </TrueBranch>
                        <FalseBranch>
                          <Action ActionType="3" Name="Action5" Key="Action126">
                            <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueComponentValue" Value="HTN$$C6$$" />
                          </Action>
                          <Action ActionType="1" Name="DM" Key="Condition94">
                            <ActionProperty Name="IfConnectionLogic" Value="1" />
                            <Checks>
                              <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                                <CheckProperty Name="IfCheckRuleID" Value="56" />
                              </Check>
                            </Checks>
                            <TrueBranch>
                              <Action ActionType="3" Name="Action6" Key="Action86">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="HTN$$C5$$DM$$C6$$" />
                              </Action>
                            </TrueBranch>
                            <FalseBranch>
                              <Action ActionType="3" Name="Action6" Key="Action85">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="HTN$$C6$$" />
                              </Action>
                            </FalseBranch>
                          </Action>
                        </FalseBranch>
                      </Action>
                    </FalseBranch>
                  </Action>
                </TrueBranch>
                <FalseBranch>
                  <Action ActionType="3" Name="Action3" Key="Action186">
                    <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                    <ActionProperty Name="SetValueOptions" Value="1" />
                    <ActionProperty Name="SetValueWhich" Value="1" />
                    <ActionProperty Name="SetValueComponentID" Value="Screening" />
                    <ActionProperty Name="SetValueComponentValue" Value="$$C6$$" />
                  </Action>
                  <Action ActionType="1" Name="HLD" Key="Condition95">
                    <ActionProperty Name="IfConnectionLogic" Value="1" />
                    <Checks>
                      <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                        <CheckProperty Name="IfCheckRuleID" Value="57" />
                      </Check>
                    </Checks>
                    <TrueBranch>
                      <Action ActionType="3" Name="Action4" Key="Action62">
                        <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                        <ActionProperty Name="SetValueOptions" Value="1" />
                        <ActionProperty Name="SetValueWhich" Value="1" />
                        <ActionProperty Name="SetValueComponentID" Value="Screening" />
                        <ActionProperty Name="SetValueComponentValue" Value="HLD$$C6$$" />
                      </Action>
                      <Action ActionType="1" Name="TAD" Key="Condition96">
                        <ActionProperty Name="IfConnectionLogic" Value="1" />
                        <Checks>
                          <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                            <CheckProperty Name="IfCheckRuleID" Value="58" />
                          </Check>
                        </Checks>
                        <TrueBranch>
                          <Action ActionType="3" Name="Action5" Key="Action124">
                            <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueComponentValue" Value="HLD$$C5$$Tobacco\Drug\Alcohol$$C6$$" />
                          </Action>
                          <Action ActionType="1" Name="DM" Key="Condition97">
                            <ActionProperty Name="IfConnectionLogic" Value="1" />
                            <Checks>
                              <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                                <CheckProperty Name="IfCheckRuleID" Value="59" />
                              </Check>
                            </Checks>
                            <TrueBranch>
                              <Action ActionType="3" Name="Action6" Key="Action84">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="HLD$$C5$$Tobacco\Drug\Alcohol$$C5$$DM$$C6$$" />
                              </Action>
                            </TrueBranch>
                            <FalseBranch>
                              <Action ActionType="3" Name="Action6" Key="Action83">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="HLD$$C5$$Tobacco\Drug\Alcohol$$C6$$" />
                              </Action>
                            </FalseBranch>
                          </Action>
                        </TrueBranch>
                        <FalseBranch>
                          <Action ActionType="3" Name="Action5" Key="Action123">
                            <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueComponentValue" Value="HLD$$C6$$" />
                          </Action>
                          <Action ActionType="1" Name="DM" Key="Condition98">
                            <ActionProperty Name="IfConnectionLogic" Value="1" />
                            <Checks>
                              <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                                <CheckProperty Name="IfCheckRuleID" Value="60" />
                              </Check>
                            </Checks>
                            <TrueBranch>
                              <Action ActionType="3" Name="Action6" Key="Action82">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="HLD$$C5$$DM$$C6$$" />
                              </Action>
                            </TrueBranch>
                            <FalseBranch>
                              <Action ActionType="3" Name="Action6" Key="Action81">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="HLD$$C6$$" />
                              </Action>
                            </FalseBranch>
                          </Action>
                        </FalseBranch>
                      </Action>
                    </TrueBranch>
                    <FalseBranch>
                      <Action ActionType="3" Name="Action4" Key="Action67">
                        <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                        <ActionProperty Name="SetValueOptions" Value="1" />
                        <ActionProperty Name="SetValueWhich" Value="1" />
                        <ActionProperty Name="SetValueComponentID" Value="Screening" />
                        <ActionProperty Name="SetValueComponentValue" Value="$$C6$$" />
                      </Action>
                      <Action ActionType="1" Name="TAD" Key="Condition99">
                        <ActionProperty Name="IfConnectionLogic" Value="1" />
                        <Checks>
                          <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                            <CheckProperty Name="IfCheckRuleID" Value="61" />
                          </Check>
                        </Checks>
                        <TrueBranch>
                          <Action ActionType="3" Name="Action5" Key="Action96">
                            <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueComponentValue" Value="Tobacco\Drug\Alcohol$$C6$$" />
                          </Action>
                          <Action ActionType="1" Name="DM" Key="Condition100">
                            <ActionProperty Name="IfConnectionLogic" Value="1" />
                            <Checks>
                              <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                                <CheckProperty Name="IfCheckRuleID" Value="62" />
                              </Check>
                            </Checks>
                            <TrueBranch>
                              <Action ActionType="3" Name="Action6" Key="Action80">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Tobacco\Drug\Alcohol$$C5$$DM$$C6$$" />
                              </Action>
                            </TrueBranch>
                            <FalseBranch>
                              <Action ActionType="3" Name="Action6" Key="Action79">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="Tobacco\Drug\Alcohol$$C6$$" />
                              </Action>
                            </FalseBranch>
                          </Action>
                        </TrueBranch>
                        <FalseBranch>
                          <Action ActionType="3" Name="Action5" Key="Action72">
                            <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="Screening" />
                            <ActionProperty Name="SetValueComponentValue" Value="$$C6$$" />
                          </Action>
                          <Action ActionType="1" Name="DM" Key="Condition101">
                            <ActionProperty Name="IfConnectionLogic" Value="1" />
                            <Checks>
                              <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                                <CheckProperty Name="IfCheckRuleID" Value="63" />
                              </Check>
                            </Checks>
                            <TrueBranch>
                              <Action ActionType="3" Name="Action6" Key="Action78">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="DM$$C6$$" />
                              </Action>
                            </TrueBranch>
                            <FalseBranch>
                              <Action ActionType="3" Name="Action6" Key="Action77">
                                <ActionProperty Name="SetValueRealComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueOptions" Value="1" />
                                <ActionProperty Name="SetValueWhich" Value="1" />
                                <ActionProperty Name="SetValueComponentID" Value="Screening" />
                                <ActionProperty Name="SetValueComponentValue" Value="None$$C6$$" />
                              </Action>
                              <Action ActionType="4" Name="Action65" Key="Action65">
                                <ActionProperty Name="SetPropertyRealComponentID" Value="Cell45" />
                                <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                                <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
                                <ActionProperty Name="SetPropertyComponentID" Value="Screening" />
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
      <Action ActionType="1" Name="ASCVD" Key="Condition1">
        <ActionProperty Name="IfConnectionLogic" Value="1" />
        <Checks>
          <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckRuleID" Value="64" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="3" Name="ASCVDChoice" Key="Action1">
            <ActionProperty Name="SetValueRealComponentID" Value="HxofASCVD" />
            <ActionProperty Name="SetValueWhich" Value="1" />
            <ActionProperty Name="SetValueComponentID" Value="HxofASCVD" />
            <ActionProperty Name="SetValueComponentValue" Value="Yes$$C6$$" />
          </Action>
        </TrueBranch>
        <FalseBranch>
          <Action ActionType="3" Name="ASCVDChoice" Key="Action2">
            <ActionProperty Name="SetValueRealComponentID" Value="HxofASCVD" />
            <ActionProperty Name="SetValueWhich" Value="1" />
            <ActionProperty Name="SetValueComponentID" Value="HxofASCVD" />
            <ActionProperty Name="SetValueComponentValue" Value="No$$C6$$" />
          </Action>
        </FalseBranch>
      </Action>
      <Action ActionType="1" Name="DM" Key="Condition2">
        <ActionProperty Name="IfConnectionLogic" Value="1" />
        <Checks>
          <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckRuleID" Value="65" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="3" Name="DMChoice" Key="Action3">
            <ActionProperty Name="SetValueRealComponentID" Value="Diabetes" />
            <ActionProperty Name="SetValueWhich" Value="1" />
            <ActionProperty Name="SetValueComponentID" Value="Diabetes" />
            <ActionProperty Name="SetValueComponentValue" Value="Yes$$C6$$" />
          </Action>
        </TrueBranch>
        <FalseBranch>
          <Action ActionType="3" Name="DMChoice" Key="Action4">
            <ActionProperty Name="SetValueRealComponentID" Value="Diabetes" />
            <ActionProperty Name="SetValueWhich" Value="1" />
            <ActionProperty Name="SetValueComponentID" Value="Diabetes" />
            <ActionProperty Name="SetValueComponentValue" Value="No$$C6$$" />
          </Action>
        </FalseBranch>
      </Action>
      <Action ActionType="1" Name="Sex" Key="Condition3">
        <ActionProperty Name="IfConnectionLogic" Value="1" />
        <Checks>
          <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckRuleID" Value="66" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="3" Name="F" Key="Action5">
            <ActionProperty Name="SetValueRealComponentID" Value="Sex" />
            <ActionProperty Name="SetValueWhich" Value="1" />
            <ActionProperty Name="SetValueComponentID" Value="Sex" />
            <ActionProperty Name="SetValueComponentValue" Value="Female$$C6$$" />
          </Action>
        </TrueBranch>
        <FalseBranch>
          <Action ActionType="1" Name="Condition2" Key="Condition4">
            <ActionProperty Name="IfConnectionLogic" Value="1" />
            <Checks>
              <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                <CheckProperty Name="IfCheckRuleID" Value="67" />
              </Check>
            </Checks>
            <TrueBranch>
              <Action ActionType="3" Name="M" Key="Action6">
                <ActionProperty Name="SetValueRealComponentID" Value="Sex" />
                <ActionProperty Name="SetValueWhich" Value="1" />
                <ActionProperty Name="SetValueComponentID" Value="Sex" />
                <ActionProperty Name="SetValueComponentValue" Value="Male$$C6$$" />
              </Action>
            </TrueBranch>
            <FalseBranch>
              <Action ActionType="3" Name="X" Key="Action7">
                <ActionProperty Name="SetValueRealComponentID" Value="Sex" />
                <ActionProperty Name="SetValueWhich" Value="1" />
                <ActionProperty Name="SetValueComponentID" Value="Sex" />
                <ActionProperty Name="SetValueComponentValue" Value="X$$C6$$" />
              </Action>
            </FalseBranch>
          </Action>
        </FalseBranch>
      </Action>
      <Action ActionType="1" Name="Smoker" Key="Condition5">
        <ActionProperty Name="IfConnectionLogic" Value="1" />
        <Checks>
          <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckRuleID" Value="68" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="3" Name="SmokerChoice" Key="Action8">
            <ActionProperty Name="SetValueRealComponentID" Value="Smoker" />
            <ActionProperty Name="SetValueWhich" Value="1" />
            <ActionProperty Name="SetValueComponentID" Value="Smoker" />
            <ActionProperty Name="SetValueComponentValue" Value="Yes$$C6$$" />
          </Action>
        </TrueBranch>
        <FalseBranch>
          <Action ActionType="3" Name="SmokerChoice" Key="Action9">
            <ActionProperty Name="SetValueRealComponentID" Value="Smoker" />
            <ActionProperty Name="SetValueWhich" Value="1" />
            <ActionProperty Name="SetValueComponentID" Value="Smoker" />
            <ActionProperty Name="SetValueComponentValue" Value="No$$C6$$" />
          </Action>
        </FalseBranch>
      </Action>
      <Action ActionType="1" Name="Lipid Panel" Key="Condition6">
        <ActionProperty Name="IfConnectionLogic" Value="1" />
        <Checks>
          <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckRuleID" Value="69" />
          </Check>
        </Checks>
        <FalseBranch>
          <Action ActionType="4" Name="Action14" Key="Action16">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell31" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="Label3" />
          </Action>
        </FalseBranch>
      </Action>
    </Script>
    <Script Name="ASCVD10_ValueChanged" ProcType="3" CreationType="2" ParamCount="0" Component="">
      <Action ActionType="1" Name="ModRiskVis" Key="Condition1">
        <ActionProperty Name="IfConnectionLogicType" Value="2" />
        <ActionProperty Name="IfConnectionLogic" Value="1 AND 3 AND 2" />
        <Checks>
          <Check CheckType="2" Name="Check1" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="ASCVD10" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="ASCVD10" />
            <CheckProperty Name="IfCheckValueOperator" Value="3" />
            <CheckProperty Name="IfCheckValueValue" Value="0$$C6$$" />
          </Check>
          <Check CheckType="2" Name="Check2" Key="Check3" CheckNum="3">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueOperator" Value="8" />
            <CheckProperty Name="IfCheckValueValue" Value="$$C6$$" />
          </Check>
          <Check CheckType="2" Name="Check2" Key="Check2" CheckNum="2">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueOperator" Value="2" />
            <CheckProperty Name="IfCheckValueValue" Value="None$$C6$$" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="4" Name="Action1" Key="Action1">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell21" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="ModifiableRisk" />
          </Action>
        </TrueBranch>
        <FalseBranch>
          <Action ActionType="4" Name="Action1" Key="Action2">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell21" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="ModifiableRisk" />
          </Action>
        </FalseBranch>
      </Action>
    </Script>
    <Script Name="CVD10_ValueChanged" ProcType="3" CreationType="2" ParamCount="0" Component="">
      <Action ActionType="1" Name="CVD10" Key="Condition1">
        <ActionProperty Name="IfConnectionLogic" Value="1" />
        <Checks>
          <Check CheckType="2" Name="Check1" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="CVD10" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="CVD10" />
            <CheckProperty Name="IfCheckValueOperator" Value="3" />
            <CheckProperty Name="IfCheckValueValue" Value="0$$C6$$" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="1" Name="Low" Key="Condition2">
            <ActionProperty Name="IfConnectionLogic" Value="1 AND 2" />
            <Checks>
              <Check CheckType="2" Name="Check1" Key="Check1" CheckNum="1">
                <CheckProperty Name="IfCheckValueWhich" Value="1" />
                <CheckProperty Name="IfCheckValueComponentID" Value="CVD10" />
                <CheckProperty Name="IfCheckValueRealComponentID" Value="CVD10" />
                <CheckProperty Name="IfCheckValueOperator" Value="4" />
                <CheckProperty Name="IfCheckValueValue" Value="5$$C6$$" />
              </Check>
              <Check CheckType="2" Name="Check2" Key="Check2" CheckNum="2">
                <CheckProperty Name="IfCheckValueWhich" Value="1" />
                <CheckProperty Name="IfCheckValueComponentID" Value="CVD10" />
                <CheckProperty Name="IfCheckValueRealComponentID" Value="CVD10" />
                <CheckProperty Name="IfCheckValueOperator" Value="3" />
                <CheckProperty Name="IfCheckValueValue" Value="0$$C6$$" />
              </Check>
            </Checks>
            <TrueBranch>
              <Action ActionType="4" Name="Action1" Key="Action1">
                <ActionProperty Name="SetPropertyRealComponentID" Value="Cell94" />
                <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
                <ActionProperty Name="SetPropertyComponentID" Value="Risk0" />
              </Action>
              <Action ActionType="4" Name="Action1" Key="Action2">
                <ActionProperty Name="SetPropertyRealComponentID" Value="Cell98" />
                <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                <ActionProperty Name="SetPropertyComponentID" Value="Risk2" />
              </Action>
              <Action ActionType="4" Name="Action1" Key="Action3">
                <ActionProperty Name="SetPropertyRealComponentID" Value="Cell100" />
                <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                <ActionProperty Name="SetPropertyComponentID" Value="Risk3" />
              </Action>
              <Action ActionType="4" Name="Action1" Key="Action4">
                <ActionProperty Name="SetPropertyRealComponentID" Value="Cell102" />
                <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                <ActionProperty Name="SetPropertyComponentID" Value="Risk4" />
              </Action>
            </TrueBranch>
            <FalseBranch>
              <Action ActionType="1" Name="Borderline" Key="Condition3">
                <ActionProperty Name="IfConnectionLogic" Value="1 AND 2" />
                <Checks>
                  <Check CheckType="2" Name="Check1" Key="Check1" CheckNum="1">
                    <CheckProperty Name="IfCheckValueWhich" Value="1" />
                    <CheckProperty Name="IfCheckValueComponentID" Value="CVD10" />
                    <CheckProperty Name="IfCheckValueRealComponentID" Value="CVD10" />
                    <CheckProperty Name="IfCheckValueOperator" Value="5" />
                    <CheckProperty Name="IfCheckValueValue" Value="5$$C6$$" />
                  </Check>
                  <Check CheckType="2" Name="Check2" Key="Check2" CheckNum="2">
                    <CheckProperty Name="IfCheckValueWhich" Value="1" />
                    <CheckProperty Name="IfCheckValueComponentID" Value="CVD10" />
                    <CheckProperty Name="IfCheckValueRealComponentID" Value="CVD10" />
                    <CheckProperty Name="IfCheckValueOperator" Value="4" />
                    <CheckProperty Name="IfCheckValueValue" Value="7.5$$C6$$" />
                  </Check>
                </Checks>
                <TrueBranch>
                  <Action ActionType="4" Name="Action1" Key="Action5">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="Cell98" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                    <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
                    <ActionProperty Name="SetPropertyComponentID" Value="Risk2" />
                  </Action>
                  <Action ActionType="4" Name="Action1" Key="Action6">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="Cell94" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                    <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                    <ActionProperty Name="SetPropertyComponentID" Value="Risk0" />
                  </Action>
                  <Action ActionType="4" Name="Action1" Key="Action7">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="Cell100" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                    <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                    <ActionProperty Name="SetPropertyComponentID" Value="Risk3" />
                  </Action>
                  <Action ActionType="4" Name="Action1" Key="Action8">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="Cell102" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                    <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                    <ActionProperty Name="SetPropertyComponentID" Value="Risk4" />
                  </Action>
                </TrueBranch>
                <FalseBranch>
                  <Action ActionType="1" Name="Intermediate" Key="Condition4">
                    <ActionProperty Name="IfConnectionLogic" Value="1 AND 2" />
                    <Checks>
                      <Check CheckType="2" Name="Check1" Key="Check1" CheckNum="1">
                        <CheckProperty Name="IfCheckValueWhich" Value="1" />
                        <CheckProperty Name="IfCheckValueComponentID" Value="CVD10" />
                        <CheckProperty Name="IfCheckValueRealComponentID" Value="CVD10" />
                        <CheckProperty Name="IfCheckValueOperator" Value="5" />
                        <CheckProperty Name="IfCheckValueValue" Value="7.5$$C6$$" />
                      </Check>
                      <Check CheckType="2" Name="Check2" Key="Check2" CheckNum="2">
                        <CheckProperty Name="IfCheckValueWhich" Value="1" />
                        <CheckProperty Name="IfCheckValueComponentID" Value="CVD10" />
                        <CheckProperty Name="IfCheckValueRealComponentID" Value="CVD10" />
                        <CheckProperty Name="IfCheckValueOperator" Value="4" />
                        <CheckProperty Name="IfCheckValueValue" Value="20$$C6$$" />
                      </Check>
                    </Checks>
                    <TrueBranch>
                      <Action ActionType="4" Name="Action1" Key="Action9">
                        <ActionProperty Name="SetPropertyRealComponentID" Value="Cell100" />
                        <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                        <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
                        <ActionProperty Name="SetPropertyComponentID" Value="Risk3" />
                      </Action>
                      <Action ActionType="4" Name="Action1" Key="Action10">
                        <ActionProperty Name="SetPropertyRealComponentID" Value="Cell102" />
                        <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                        <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                        <ActionProperty Name="SetPropertyComponentID" Value="Risk4" />
                      </Action>
                      <Action ActionType="4" Name="Action1" Key="Action11">
                        <ActionProperty Name="SetPropertyRealComponentID" Value="Cell94" />
                        <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                        <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                        <ActionProperty Name="SetPropertyComponentID" Value="Risk0" />
                      </Action>
                      <Action ActionType="4" Name="Action1" Key="Action12">
                        <ActionProperty Name="SetPropertyRealComponentID" Value="Cell98" />
                        <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                        <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                        <ActionProperty Name="SetPropertyComponentID" Value="Risk2" />
                      </Action>
                    </TrueBranch>
                    <FalseBranch>
                      <Action ActionType="1" Name="High" Key="Condition5">
                        <ActionProperty Name="IfConnectionLogic" Value="1" />
                        <Checks>
                          <Check CheckType="2" Name="Check1" Key="Check1" CheckNum="1">
                            <CheckProperty Name="IfCheckValueWhich" Value="1" />
                            <CheckProperty Name="IfCheckValueComponentID" Value="CVD10" />
                            <CheckProperty Name="IfCheckValueRealComponentID" Value="CVD10" />
                            <CheckProperty Name="IfCheckValueOperator" Value="5" />
                            <CheckProperty Name="IfCheckValueValue" Value="20$$C6$$" />
                          </Check>
                        </Checks>
                        <TrueBranch>
                          <Action ActionType="4" Name="Action1" Key="Action13">
                            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell102" />
                            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
                            <ActionProperty Name="SetPropertyComponentID" Value="Risk4" />
                          </Action>
                          <Action ActionType="4" Name="Action1" Key="Action14">
                            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell100" />
                            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                            <ActionProperty Name="SetPropertyComponentID" Value="Risk3" />
                          </Action>
                          <Action ActionType="4" Name="Action1" Key="Action15">
                            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell98" />
                            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                            <ActionProperty Name="SetPropertyComponentID" Value="Risk2" />
                          </Action>
                          <Action ActionType="4" Name="Action1" Key="Action16">
                            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell94" />
                            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                            <ActionProperty Name="SetPropertyComponentID" Value="Risk0" />
                          </Action>
                        </TrueBranch>
                      </Action>
                    </FalseBranch>
                  </Action>
                </FalseBranch>
              </Action>
            </FalseBranch>
          </Action>
        </TrueBranch>
        <FalseBranch>
          <Action ActionType="4" Name="Action1" Key="Action18">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell94" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="Risk0" />
          </Action>
          <Action ActionType="4" Name="Action1" Key="Action17">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell102" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="Risk4" />
          </Action>
          <Action ActionType="4" Name="Action1" Key="Action19">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell100" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="Risk3" />
          </Action>
          <Action ActionType="4" Name="Action1" Key="Action20">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell94" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="Risk0" />
          </Action>
        </FalseBranch>
      </Action>
      <Action ActionType="1" Name="RiskManagement" Key="Condition6">
        <ActionProperty Name="IfConnectionLogicType" Value="2" />
        <ActionProperty Name="IfConnectionLogic" Value="8 AND 10 AND 11 AND 9 AND NOT 1" />
        <Checks>
          <Check CheckType="2" Name="HxofASCVD" Key="Check8" CheckNum="8">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="HxofASCVD" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="HxofASCVD" />
            <CheckProperty Name="IfCheckValueOperator" Value="1" />
            <CheckProperty Name="IfCheckValueValue" Value="No$$C6$$" />
          </Check>
          <Check CheckType="1" Name="Check10" Key="Check10" CheckNum="10">
            <CheckProperty Name="IfCheckPropComponentID" Value="SimASCVd" />
            <CheckProperty Name="IfCheckPropRealComponentID" Value="Cell19" />
            <CheckProperty Name="IfCheckPropProperty" Value="Visible" />
            <CheckProperty Name="IfCheckPropValue" Value="True" />
          </Check>
          <Check CheckType="1" Name="Check11" Key="Check11" CheckNum="11">
            <CheckProperty Name="IfCheckPropComponentID" Value="RiskEnhancers" />
            <CheckProperty Name="IfCheckPropRealComponentID" Value="Cell22" />
            <CheckProperty Name="IfCheckPropProperty" Value="Visible" />
            <CheckProperty Name="IfCheckPropValue" Value="True" />
          </Check>
          <Check CheckType="2" Name="Check9" Key="Check9" CheckNum="9">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="CVD10" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="CVD10" />
            <CheckProperty Name="IfCheckValueOperator" Value="5" />
            <CheckProperty Name="IfCheckValueValue" Value="7.5$$C6$$" />
          </Check>
          <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckRuleID" Value="70" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="4" Name="Action14" Key="Action21">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell36" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="ASCVDRiskManagement" />
          </Action>
          <Action ActionType="4" Name="Action14" Key="Action23">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell37" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="ASCVDRiskManText" />
          </Action>
        </TrueBranch>
        <FalseBranch>
          <Action ActionType="4" Name="Action14" Key="Action22">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell36" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="ASCVDRiskManagement" />
          </Action>
          <Action ActionType="4" Name="Action14" Key="Action24">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell37" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="ASCVDRiskManText" />
          </Action>
        </FalseBranch>
      </Action>
    </Script>
    <Script Name="Diabetes_ValueChanged" ProcType="3" CreationType="2" ParamCount="0" Component="">
      <Action ActionType="1" Name="DMCheck" Key="Condition1">
        <ActionProperty Name="IfConnectionLogicType" Value="1" />
        <ActionProperty Name="IfConnectionLogic" Value="1" />
        <Checks>
          <Check CheckType="2" Name="Check1" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="Glycemic Control$$C6$$" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="3" Name="Action17" Key="Action2">
            <ActionProperty Name="SetValueRealComponentID" Value="SimDM" />
            <ActionProperty Name="SetValueOptions" Value="1" />
            <ActionProperty Name="SetValueWhich" Value="1" />
            <ActionProperty Name="SetValueComponentID" Value="SimDM" />
            <ActionProperty Name="SetValueComponentValue" Value="No$$C6$$" />
          </Action>
        </TrueBranch>
        <FalseBranch>
          <Action ActionType="1" Name="Condition6" Key="Condition2">
            <ActionProperty Name="IfConnectionLogic" Value="1" />
            <Checks>
              <Check CheckType="2" Name="Check1" Key="Check1" CheckNum="1">
                <CheckProperty Name="IfCheckValueWhich" Value="1" />
                <CheckProperty Name="IfCheckValueComponentID" Value="Diabetes" />
                <CheckProperty Name="IfCheckValueRealComponentID" Value="Diabetes" />
                <CheckProperty Name="IfCheckValueOperator" Value="1" />
                <CheckProperty Name="IfCheckValueValue" Value="Yes$$C6$$" />
              </Check>
            </Checks>
            <TrueBranch>
              <Action ActionType="3" Name="Action17" Key="Action4">
                <ActionProperty Name="SetValueRealComponentID" Value="SimDM" />
                <ActionProperty Name="SetValueOptions" Value="1" />
                <ActionProperty Name="SetValueWhich" Value="1" />
                <ActionProperty Name="SetValueComponentID" Value="SimDM" />
                <ActionProperty Name="SetValueComponentValue" Value="Yes$$C6$$" />
              </Action>
            </TrueBranch>
            <FalseBranch>
              <Action ActionType="3" Name="Action17" Key="Action5">
                <ActionProperty Name="SetValueRealComponentID" Value="SimDM" />
                <ActionProperty Name="SetValueOptions" Value="1" />
                <ActionProperty Name="SetValueWhich" Value="1" />
                <ActionProperty Name="SetValueComponentID" Value="SimDM" />
                <ActionProperty Name="SetValueComponentValue" Value="No$$C6$$" />
              </Action>
            </FalseBranch>
          </Action>
        </FalseBranch>
      </Action>
    </Script>
    <Script Name="HF10_ValueChanged" ProcType="3" CreationType="2" ParamCount="0" Component="">
      <Action ActionType="1" Name="HF Domains" Key="Condition1">
        <ActionProperty Name="IfConnectionLogic" Value="1" />
        <Checks>
          <Check CheckType="2" Name="Check1" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="HF10" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="HF10" />
            <CheckProperty Name="IfCheckValueOperator" Value="1" />
            <CheckProperty Name="IfCheckValueValue" Value="0$$C6$$" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="1" Name="Condition2" Key="Condition2">
            <ActionProperty Name="IfConnectionLogic" Value="1" />
            <Checks>
              <Check CheckType="2" Name="Check1" Key="Check1" CheckNum="1">
                <CheckProperty Name="IfCheckValueWhich" Value="1" />
                <CheckProperty Name="IfCheckValueComponentID" Value="CVD10" />
                <CheckProperty Name="IfCheckValueRealComponentID" Value="CVD10" />
                <CheckProperty Name="IfCheckValueOperator" Value="1" />
                <CheckProperty Name="IfCheckValueValue" Value="0$$C6$$" />
              </Check>
            </Checks>
            <TrueBranch>
              <Action ActionType="4" Name="Action1" Key="Action1">
                <ActionProperty Name="SetPropertyRealComponentID" Value="Cell75" />
                <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
                <ActionProperty Name="SetPropertyComponentID" Value="VariableHF" />
              </Action>
            </TrueBranch>
            <FalseBranch>
              <Action ActionType="4" Name="Action1" Key="Action3">
                <ActionProperty Name="SetPropertyRealComponentID" Value="Cell75" />
                <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
                <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
                <ActionProperty Name="SetPropertyComponentID" Value="VariableHF" />
              </Action>
            </FalseBranch>
          </Action>
        </TrueBranch>
        <FalseBranch>
          <Action ActionType="4" Name="Action1" Key="Action2">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell75" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="VariableHF" />
          </Action>
        </FalseBranch>
      </Action>
    </Script>
    <Script Name="Screening_ValueChangedNotByLoad" ProcType="3" CreationType="2" ParamCount="0" Component="">
      <Action ActionType="1" Name="Sim" Key="Condition1">
        <ActionProperty Name="IfConnectionLogic" Value="1" />
        <Checks>
          <Check CheckType="1" Name="Check1" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckPropComponentID" Value="SimTitle" />
            <CheckProperty Name="IfCheckPropRealComponentID" Value="Cell99" />
            <CheckProperty Name="IfCheckPropProperty" Value="Visible" />
            <CheckProperty Name="IfCheckPropValue" Value="True" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="6" Name="DifCVD" Key="Action1">
            <ActionProperty Name="CalculateExpression" Value="SimCVD -  CVD10  " />
            <ActionProperty Name="CalculateRequireAllVariables" Value="True" />
            <ActionProperty Name="SetValueRealComponentID" Value="DifCVD" />
            <ActionProperty Name="CalculateClearWhenMissingVars" Value="False" />
            <ActionProperty Name="SetValueComponentID" Value="DifCVD" />
          </Action>
          <Action ActionType="1" Name="DifCVD &gt; 0 " Key="Condition2">
            <ActionProperty Name="IfConnectionLogic" Value="1" />
            <Checks>
              <Check CheckType="1" Name="Check1" Key="Check1" CheckNum="1">
                <CheckProperty Name="IfCheckPropComponentID" Value="DifCVD" />
                <CheckProperty Name="IfCheckPropRealComponentID" Value="DifCVD" />
                <CheckProperty Name="IfCheckPropProperty" Value="Caption" />
                <CheckProperty Name="IfCheckPropValue" Value="0" />
              </Check>
            </Checks>
            <TrueBranch>
              <Action ActionType="6" Name="HFSignNull" Key="Action2">
                <ActionProperty Name="CalculateExpression" Value="0" />
                <ActionProperty Name="CalculateRequireAllVariables" Value="False" />
                <ActionProperty Name="SetValueRealComponentID" Value="SignCVD" />
                <ActionProperty Name="CalculateClearWhenMissingVars" Value="False" />
                <ActionProperty Name="SetValueComponentID" Value="SignCVD" />
              </Action>
            </TrueBranch>
            <FalseBranch>
              <Action ActionType="6" Name="Action1" Key="Action3">
                <ActionProperty Name="CalculateExpression" Value="(SimCVD-CVD10+0.001)/(((SimCVD-CVD10+0.001) ^ 2)^(1/2))" />
                <ActionProperty Name="CalculateRequireAllVariables" Value="True" />
                <ActionProperty Name="SetValueRealComponentID" Value="SignCVD" />
                <ActionProperty Name="CalculateClearWhenMissingVars" Value="False" />
                <ActionProperty Name="SetValueComponentID" Value="SignCVD" />
              </Action>
            </FalseBranch>
          </Action>
        </TrueBranch>
        <FalseBranch>
          <Action ActionType="6" Name="HFSignNull" Key="Action4">
            <ActionProperty Name="CalculateExpression" Value="0" />
            <ActionProperty Name="CalculateRequireAllVariables" Value="False" />
            <ActionProperty Name="SetValueRealComponentID" Value="SignCVD" />
            <ActionProperty Name="CalculateClearWhenMissingVars" Value="False" />
            <ActionProperty Name="SetValueComponentID" Value="SignCVD" />
          </Action>
        </FalseBranch>
      </Action>
      <Action ActionType="1" Name="Flag Decrease" Key="Condition3">
        <ActionProperty Name="IfConnectionLogic" Value="1" />
        <Checks>
          <Check CheckType="1" Name="Check1" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckPropComponentID" Value="SignCVD" />
            <CheckProperty Name="IfCheckPropRealComponentID" Value="SignCVD" />
            <CheckProperty Name="IfCheckPropProperty" Value="Caption" />
            <CheckProperty Name="IfCheckPropValue" Value="-1" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="4" Name="SimCVA" Key="Action5">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell27" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="#80FF80" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimCVA" />
          </Action>
          <Action ActionType="4" Name="SimCHD" Key="Action6">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell26" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="#80FF80" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimCHD" />
          </Action>
          <Action ActionType="4" Name="SimCVD" Key="Action7">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell20" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="#80FF80" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimCVD" />
          </Action>
          <Action ActionType="4" Name="SimASCVD" Key="Action8">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell19" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="#80FF80" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimASCVd" />
          </Action>
          <Action ActionType="4" Name="per1" Key="Action9">
            <ActionProperty Name="SetPropertyRealComponentID" Value="per1" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="#80FF80" />
            <ActionProperty Name="SetPropertyComponentID" Value="per1" />
          </Action>
          <Action ActionType="4" Name="per2" Key="Action10">
            <ActionProperty Name="SetPropertyRealComponentID" Value="per2" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="#80FF80" />
            <ActionProperty Name="SetPropertyComponentID" Value="per2" />
          </Action>
          <Action ActionType="4" Name="per3" Key="Action11">
            <ActionProperty Name="SetPropertyRealComponentID" Value="per3" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="#80FF80" />
            <ActionProperty Name="SetPropertyComponentID" Value="per3" />
          </Action>
          <Action ActionType="4" Name="per4" Key="Action12">
            <ActionProperty Name="SetPropertyRealComponentID" Value="per4" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="#80FF80" />
            <ActionProperty Name="SetPropertyComponentID" Value="per4" />
          </Action>
        </TrueBranch>
        <FalseBranch>
          <Action ActionType="1" Name="Increase" Key="Condition4">
            <ActionProperty Name="IfConnectionLogic" Value="2" />
            <Checks>
              <Check CheckType="1" Name="Check1" Key="Check2" CheckNum="2">
                <CheckProperty Name="IfCheckPropComponentID" Value="SignCVD" />
                <CheckProperty Name="IfCheckPropRealComponentID" Value="SignCVD" />
                <CheckProperty Name="IfCheckPropProperty" Value="Caption" />
                <CheckProperty Name="IfCheckPropValue" Value="1" />
              </Check>
            </Checks>
            <TrueBranch>
              <Action ActionType="4" Name="SimASCVD" Key="Action13">
                <ActionProperty Name="SetPropertyRealComponentID" Value="Cell19" />
                <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                <ActionProperty Name="SetPropertyPropertyValue" Value="#FF0000" />
                <ActionProperty Name="SetPropertyComponentID" Value="SimASCVd" />
              </Action>
              <Action ActionType="4" Name="SimCVA" Key="Action14">
                <ActionProperty Name="SetPropertyRealComponentID" Value="Cell27" />
                <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                <ActionProperty Name="SetPropertyPropertyValue" Value="#FF0000" />
                <ActionProperty Name="SetPropertyComponentID" Value="SimCVA" />
              </Action>
              <Action ActionType="4" Name="SimCHD" Key="Action15">
                <ActionProperty Name="SetPropertyRealComponentID" Value="Cell26" />
                <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                <ActionProperty Name="SetPropertyPropertyValue" Value="#FF0000" />
                <ActionProperty Name="SetPropertyComponentID" Value="SimCHD" />
              </Action>
              <Action ActionType="4" Name="per3" Key="Action16">
                <ActionProperty Name="SetPropertyRealComponentID" Value="per3" />
                <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                <ActionProperty Name="SetPropertyPropertyValue" Value="#FF0000" />
                <ActionProperty Name="SetPropertyComponentID" Value="per3" />
              </Action>
              <Action ActionType="4" Name="per1" Key="Action17">
                <ActionProperty Name="SetPropertyRealComponentID" Value="per1" />
                <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                <ActionProperty Name="SetPropertyPropertyValue" Value="#FF0000" />
                <ActionProperty Name="SetPropertyComponentID" Value="per1" />
              </Action>
              <Action ActionType="4" Name="per2" Key="Action18">
                <ActionProperty Name="SetPropertyRealComponentID" Value="per2" />
                <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                <ActionProperty Name="SetPropertyPropertyValue" Value="#FF0000" />
                <ActionProperty Name="SetPropertyComponentID" Value="per2" />
              </Action>
              <Action ActionType="4" Name="per4" Key="Action19">
                <ActionProperty Name="SetPropertyRealComponentID" Value="per4" />
                <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                <ActionProperty Name="SetPropertyPropertyValue" Value="#FF0000" />
                <ActionProperty Name="SetPropertyComponentID" Value="per4" />
              </Action>
            </TrueBranch>
            <FalseBranch>
              <Action ActionType="1" Name="Null" Key="Condition5">
                <ActionProperty Name="IfConnectionLogic" Value="2" />
                <Checks>
                  <Check CheckType="1" Name="Check1" Key="Check2" CheckNum="2">
                    <CheckProperty Name="IfCheckPropComponentID" Value="SignCVD" />
                    <CheckProperty Name="IfCheckPropRealComponentID" Value="SignCVD" />
                    <CheckProperty Name="IfCheckPropProperty" Value="Caption" />
                    <CheckProperty Name="IfCheckPropValue" Value="0" />
                  </Check>
                </Checks>
                <TrueBranch>
                  <Action ActionType="4" Name="SimASCVD" Key="Action20">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="Cell19" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                    <ActionProperty Name="SetPropertyPropertyValue" Value="#FFFFFF" />
                    <ActionProperty Name="SetPropertyComponentID" Value="SimASCVd" />
                  </Action>
                  <Action ActionType="4" Name="SimCVD" Key="Action21">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="Cell20" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                    <ActionProperty Name="SetPropertyPropertyValue" Value="#FFFFFF" />
                    <ActionProperty Name="SetPropertyComponentID" Value="SimCVD" />
                  </Action>
                  <Action ActionType="4" Name="SimCHD" Key="Action22">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="Cell26" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                    <ActionProperty Name="SetPropertyPropertyValue" Value="#FFFFFF" />
                    <ActionProperty Name="SetPropertyComponentID" Value="SimCHD" />
                  </Action>
                  <Action ActionType="4" Name="SimCVA" Key="Action23">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="Cell27" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                    <ActionProperty Name="SetPropertyPropertyValue" Value="#FFFFFF" />
                    <ActionProperty Name="SetPropertyComponentID" Value="SimCVA" />
                  </Action>
                  <Action ActionType="4" Name="per3" Key="Action24">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="per3" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                    <ActionProperty Name="SetPropertyComponentID" Value="per3" />
                  </Action>
                  <Action ActionType="4" Name="per2" Key="Action25">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="per2" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                    <ActionProperty Name="SetPropertyComponentID" Value="per2" />
                  </Action>
                  <Action ActionType="4" Name="per4" Key="Action26">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="per4" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                    <ActionProperty Name="SetPropertyComponentID" Value="per4" />
                  </Action>
                  <Action ActionType="4" Name="per1" Key="Action27">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="per1" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                    <ActionProperty Name="SetPropertyComponentID" Value="per1" />
                  </Action>
                </TrueBranch>
                <FalseBranch>
                  <Action ActionType="4" Name="SimASCVD" Key="Action28">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="Cell19" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                    <ActionProperty Name="SetPropertyPropertyValue" Value="#FFFFFF" />
                    <ActionProperty Name="SetPropertyComponentID" Value="SimASCVd" />
                  </Action>
                  <Action ActionType="4" Name="SimCVA" Key="Action29">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="Cell27" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                    <ActionProperty Name="SetPropertyPropertyValue" Value="#FFFFFF" />
                    <ActionProperty Name="SetPropertyComponentID" Value="SimCVA" />
                  </Action>
                  <Action ActionType="4" Name="SimCHD" Key="Action30">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="Cell26" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                    <ActionProperty Name="SetPropertyPropertyValue" Value="#FFFFFF" />
                    <ActionProperty Name="SetPropertyComponentID" Value="SimCHD" />
                  </Action>
                  <Action ActionType="4" Name="SimCVD" Key="Action31">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="Cell20" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                    <ActionProperty Name="SetPropertyPropertyValue" Value="#FFFFFF" />
                    <ActionProperty Name="SetPropertyComponentID" Value="SimCVD" />
                  </Action>
                </FalseBranch>
              </Action>
            </FalseBranch>
          </Action>
        </FalseBranch>
      </Action>
      <Action ActionType="1" Name="Sim" Key="Condition6">
        <ActionProperty Name="IfConnectionLogic" Value="1" />
        <Checks>
          <Check CheckType="1" Name="Check1" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckPropComponentID" Value="SimTitle" />
            <CheckProperty Name="IfCheckPropRealComponentID" Value="Cell99" />
            <CheckProperty Name="IfCheckPropProperty" Value="Visible" />
            <CheckProperty Name="IfCheckPropValue" Value="True" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="6" Name="HFDif" Key="Action32">
            <ActionProperty Name="CalculateExpression" Value="(SimHF-HF10) " />
            <ActionProperty Name="CalculateRequireAllVariables" Value="True" />
            <ActionProperty Name="SetValueRealComponentID" Value="DifHF" />
            <ActionProperty Name="CalculateClearWhenMissingVars" Value="False" />
            <ActionProperty Name="SetValueComponentID" Value="DifHF" />
          </Action>
          <Action ActionType="1" Name="HFDif &gt; 0 " Key="Condition7">
            <ActionProperty Name="IfConnectionLogic" Value="1" />
            <Checks>
              <Check CheckType="1" Name="Check1" Key="Check1" CheckNum="1">
                <CheckProperty Name="IfCheckPropComponentID" Value="DifHF" />
                <CheckProperty Name="IfCheckPropRealComponentID" Value="DifHF" />
                <CheckProperty Name="IfCheckPropProperty" Value="Caption" />
                <CheckProperty Name="IfCheckPropValue" Value="0" />
              </Check>
            </Checks>
            <TrueBranch>
              <Action ActionType="6" Name="HFSignNull" Key="Action33">
                <ActionProperty Name="CalculateExpression" Value="0" />
                <ActionProperty Name="CalculateRequireAllVariables" Value="False" />
                <ActionProperty Name="SetValueRealComponentID" Value="SignHF" />
                <ActionProperty Name="CalculateClearWhenMissingVars" Value="False" />
                <ActionProperty Name="SetValueComponentID" Value="SignHF" />
              </Action>
            </TrueBranch>
            <FalseBranch>
              <Action ActionType="6" Name="Action1" Key="Action34">
                <ActionProperty Name="CalculateExpression" Value="(SimHF-HF10+0.001)/(((SimHF-HF10+0.001) ^ 2)^(1/2))" />
                <ActionProperty Name="CalculateRequireAllVariables" Value="True" />
                <ActionProperty Name="SetValueRealComponentID" Value="SignHF" />
                <ActionProperty Name="CalculateClearWhenMissingVars" Value="False" />
                <ActionProperty Name="SetValueComponentID" Value="SignHF" />
              </Action>
            </FalseBranch>
          </Action>
        </TrueBranch>
        <FalseBranch>
          <Action ActionType="6" Name="HFSignNull" Key="Action35">
            <ActionProperty Name="CalculateExpression" Value="0" />
            <ActionProperty Name="CalculateRequireAllVariables" Value="False" />
            <ActionProperty Name="SetValueRealComponentID" Value="SignHF" />
            <ActionProperty Name="CalculateClearWhenMissingVars" Value="False" />
            <ActionProperty Name="SetValueComponentID" Value="SignHF" />
          </Action>
        </FalseBranch>
      </Action>
      <Action ActionType="1" Name="Flag" Key="Condition8">
        <ActionProperty Name="IfConnectionLogic" Value="1" />
        <Checks>
          <Check CheckType="1" Name="Check1" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckPropComponentID" Value="SignHF" />
            <CheckProperty Name="IfCheckPropRealComponentID" Value="SignHF" />
            <CheckProperty Name="IfCheckPropProperty" Value="Caption" />
            <CheckProperty Name="IfCheckPropValue" Value="-1" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="4" Name="Reduction" Key="Action36">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell28" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="#80FF80" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimHF" />
          </Action>
          <Action ActionType="4" Name="per5" Key="Action37">
            <ActionProperty Name="SetPropertyRealComponentID" Value="per5" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="#80FF80" />
            <ActionProperty Name="SetPropertyComponentID" Value="per5" />
          </Action>
        </TrueBranch>
        <FalseBranch>
          <Action ActionType="1" Name="Condition4" Key="Condition9">
            <ActionProperty Name="IfConnectionLogic" Value="1" />
            <Checks>
              <Check CheckType="1" Name="Check1" Key="Check1" CheckNum="1">
                <CheckProperty Name="IfCheckPropComponentID" Value="SignHF" />
                <CheckProperty Name="IfCheckPropRealComponentID" Value="SignHF" />
                <CheckProperty Name="IfCheckPropProperty" Value="Caption" />
                <CheckProperty Name="IfCheckPropValue" Value="1" />
              </Check>
            </Checks>
            <TrueBranch>
              <Action ActionType="4" Name="Increase" Key="Action38">
                <ActionProperty Name="SetPropertyRealComponentID" Value="Cell28" />
                <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                <ActionProperty Name="SetPropertyPropertyValue" Value="#FF0000" />
                <ActionProperty Name="SetPropertyComponentID" Value="SimHF" />
              </Action>
              <Action ActionType="4" Name="per5" Key="Action39">
                <ActionProperty Name="SetPropertyRealComponentID" Value="per5" />
                <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                <ActionProperty Name="SetPropertyPropertyValue" Value="#80FF80" />
                <ActionProperty Name="SetPropertyComponentID" Value="per5" />
              </Action>
            </TrueBranch>
            <FalseBranch>
              <Action ActionType="1" Name="Condition4" Key="Condition10">
                <ActionProperty Name="IfConnectionLogic" Value="1" />
                <Checks>
                  <Check CheckType="1" Name="Check1" Key="Check1" CheckNum="1">
                    <CheckProperty Name="IfCheckPropComponentID" Value="SignHF" />
                    <CheckProperty Name="IfCheckPropRealComponentID" Value="SignHF" />
                    <CheckProperty Name="IfCheckPropProperty" Value="Caption" />
                    <CheckProperty Name="IfCheckPropValue" Value="0" />
                  </Check>
                </Checks>
                <TrueBranch>
                  <Action ActionType="4" Name="Null" Key="Action40">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="Cell28" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                    <ActionProperty Name="SetPropertyPropertyValue" Value="#FFFFFF" />
                    <ActionProperty Name="SetPropertyComponentID" Value="SimHF" />
                  </Action>
                  <Action ActionType="4" Name="per5" Key="Action41">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="per5" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                    <ActionProperty Name="SetPropertyPropertyValue" Value="#FFFFFF" />
                    <ActionProperty Name="SetPropertyComponentID" Value="per5" />
                  </Action>
                </TrueBranch>
                <FalseBranch>
                  <Action ActionType="4" Name="Null" Key="Action42">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="Cell28" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                    <ActionProperty Name="SetPropertyPropertyValue" Value="#FFFFFF" />
                    <ActionProperty Name="SetPropertyComponentID" Value="SimHF" />
                  </Action>
                  <Action ActionType="4" Name="per5" Key="Action43">
                    <ActionProperty Name="SetPropertyRealComponentID" Value="per5" />
                    <ActionProperty Name="SetPropertyPropertyName" Value="Back color" />
                    <ActionProperty Name="SetPropertyPropertyValue" Value="#FFFFFF" />
                    <ActionProperty Name="SetPropertyComponentID" Value="per5" />
                  </Action>
                </FalseBranch>
              </Action>
            </FalseBranch>
          </Action>
        </FalseBranch>
      </Action>
    </Script>
    <Script Name="Screening_ValueChanged" ProcType="3" CreationType="2" ParamCount="0" Component="">
      <Action ActionType="1" Name="ASCVDRisk" Key="Condition5">
        <ActionProperty Name="IfConnectionLogicType" Value="2" />
        <ActionProperty Name="IfConnectionLogic" Value="(1 OR 2 OR 3 OR 4 OR 5 OR 6 OR 7) AND (8 AND 10 AND 11 AND 9 AND (NOT 12))" />
        <Checks>
          <Check CheckType="2" Name="HxofASCVD" Key="Check8" CheckNum="8">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="HxofASCVD" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="HxofASCVD" />
            <CheckProperty Name="IfCheckValueOperator" Value="1" />
            <CheckProperty Name="IfCheckValueValue" Value="No$$C6$$" />
          </Check>
          <Check CheckType="1" Name="Check10" Key="Check10" CheckNum="10">
            <CheckProperty Name="IfCheckPropComponentID" Value="SimASCVd" />
            <CheckProperty Name="IfCheckPropRealComponentID" Value="Cell19" />
            <CheckProperty Name="IfCheckPropProperty" Value="Visible" />
            <CheckProperty Name="IfCheckPropValue" Value="True" />
          </Check>
          <Check CheckType="1" Name="Check11" Key="Check11" CheckNum="11">
            <CheckProperty Name="IfCheckPropComponentID" Value="RiskEnhancers" />
            <CheckProperty Name="IfCheckPropRealComponentID" Value="Cell22" />
            <CheckProperty Name="IfCheckPropProperty" Value="Visible" />
            <CheckProperty Name="IfCheckPropValue" Value="True" />
          </Check>
          <Check CheckType="4" Name="Check9" Key="Check9" CheckNum="9">
            <CheckProperty Name="IfCheckRuleID" Value="71" />
          </Check>
          <Check CheckType="2" Name="Obesity" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="Obesity$$C6$$" />
          </Check>
          <Check CheckType="2" Name="FamHx" Key="Check2" CheckNum="2">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="Family Hx of CVD$$C6$$" />
          </Check>
          <Check CheckType="2" Name="HTN" Key="Check3" CheckNum="3">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="HTN$$C6$$" />
          </Check>
          <Check CheckType="2" Name="HLD" Key="Check4" CheckNum="4">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="HLD$$C6$$" />
          </Check>
          <Check CheckType="2" Name="TAD" Key="Check5" CheckNum="5">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="Tobacco\Drug\Alcohol$$C6$$" />
          </Check>
          <Check CheckType="2" Name="DM" Key="Check6" CheckNum="6">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="DM$$C6$$" />
          </Check>
          <Check CheckType="2" Name="PreDM" Key="Check7" CheckNum="7">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="DM$$C6$$" />
          </Check>
          <Check CheckType="4" Name="RiskCharge" Key="Check12" CheckNum="12">
            <CheckProperty Name="IfCheckRuleID" Value="72" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="4" Name="Action3" Key="Action31">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell0" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="ASCVDRiskAssessText" />
          </Action>
          <Action ActionType="4" Name="Action14" Key="Action32">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell23" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="ASCVDRiskAssessment" />
          </Action>
        </TrueBranch>
        <FalseBranch>
          <Action ActionType="4" Name="Action14" Key="Action33">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell23" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="ASCVDRiskAssessment" />
          </Action>
          <Action ActionType="4" Name="Action3" Key="Action34">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell0" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="ASCVDRiskAssessText" />
          </Action>
        </FalseBranch>
      </Action>
      <Action ActionType="1" Name="RiskManagement" Key="Condition1">
        <ActionProperty Name="IfConnectionLogicType" Value="2" />
        <ActionProperty Name="IfConnectionLogic" Value="8 AND 10 AND 11 AND 9 AND NOT 2" />
        <Checks>
          <Check CheckType="2" Name="HxofASCVD" Key="Check8" CheckNum="8">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="HxofASCVD" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="HxofASCVD" />
            <CheckProperty Name="IfCheckValueOperator" Value="1" />
            <CheckProperty Name="IfCheckValueValue" Value="No$$C6$$" />
          </Check>
          <Check CheckType="1" Name="Check10" Key="Check10" CheckNum="10">
            <CheckProperty Name="IfCheckPropComponentID" Value="SimASCVd" />
            <CheckProperty Name="IfCheckPropRealComponentID" Value="Cell19" />
            <CheckProperty Name="IfCheckPropProperty" Value="Visible" />
            <CheckProperty Name="IfCheckPropValue" Value="True" />
          </Check>
          <Check CheckType="1" Name="Check11" Key="Check11" CheckNum="11">
            <CheckProperty Name="IfCheckPropComponentID" Value="RiskEnhancers" />
            <CheckProperty Name="IfCheckPropRealComponentID" Value="Cell22" />
            <CheckProperty Name="IfCheckPropProperty" Value="Visible" />
            <CheckProperty Name="IfCheckPropValue" Value="True" />
          </Check>
          <Check CheckType="2" Name="Check9" Key="Check9" CheckNum="9">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="CVD10" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="CVD10" />
            <CheckProperty Name="IfCheckValueOperator" Value="5" />
            <CheckProperty Name="IfCheckValueValue" Value="7.5$$C6$$" />
          </Check>
          <Check CheckType="4" Name="Charge" Key="Check2" CheckNum="2">
            <CheckProperty Name="IfCheckRuleID" Value="73" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="4" Name="Action14" Key="Action1">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell36" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="ASCVDRiskManagement" />
          </Action>
          <Action ActionType="4" Name="Action14" Key="Action2">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell37" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="ASCVDRiskManText" />
          </Action>
        </TrueBranch>
        <FalseBranch>
          <Action ActionType="4" Name="Action14" Key="Action35">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell36" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="ASCVDRiskManagement" />
          </Action>
          <Action ActionType="4" Name="Action14" Key="Action36">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell37" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="ASCVDRiskManText" />
          </Action>
        </FalseBranch>
      </Action>
      <Action ActionType="1" Name="ModRiskVis" Key="Condition3">
        <ActionProperty Name="IfConnectionLogicType" Value="2" />
        <ActionProperty Name="IfConnectionLogic" Value="1 AND 3 AND 2" />
        <Checks>
          <Check CheckType="2" Name="Check1" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="ASCVD10" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="ASCVD10" />
            <CheckProperty Name="IfCheckValueOperator" Value="3" />
            <CheckProperty Name="IfCheckValueValue" Value="0$$C6$$" />
          </Check>
          <Check CheckType="2" Name="Check2" Key="Check3" CheckNum="3">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueOperator" Value="8" />
            <CheckProperty Name="IfCheckValueValue" Value="$$C6$$" />
          </Check>
          <Check CheckType="2" Name="Check2" Key="Check2" CheckNum="2">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueOperator" Value="2" />
            <CheckProperty Name="IfCheckValueValue" Value="None$$C6$$" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="4" Name="Action1" Key="Action5">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell21" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="ModifiableRisk" />
          </Action>
        </TrueBranch>
        <FalseBranch>
          <Action ActionType="4" Name="Action1" Key="Action6">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell21" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="ModifiableRisk" />
          </Action>
        </FalseBranch>
      </Action>
      <Action ActionType="1" Name="Simulator" Key="Condition2">
        <ActionProperty Name="IfConnectionLogicType" Value="2" />
        <ActionProperty Name="IfConnectionLogic" Value="(1 OR 2 OR 3 OR 4 OR 5 OR 6 OR 7 OR 8 OR 9) AND 10 AND 11" />
        <Checks>
          <Check CheckType="2" Name="Check1" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="Blood Pressure (goal SBP &lt; 130)$$C6$$" />
          </Check>
          <Check CheckType="2" Name="Check1" Key="Check2" CheckNum="2">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="Cholesterol control$$C6$$" />
          </Check>
          <Check CheckType="2" Name="Check1" Key="Check3" CheckNum="3">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="Smoking counseling$$C6$$" />
          </Check>
          <Check CheckType="2" Name="Check1" Key="Check4" CheckNum="4">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="Alcohol reduction$$C6$$" />
          </Check>
          <Check CheckType="2" Name="Check1" Key="Check5" CheckNum="5">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="Other drug use$$C6$$" />
          </Check>
          <Check CheckType="2" Name="Check1" Key="Check6" CheckNum="6">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="Physical activity$$C6$$" />
          </Check>
          <Check CheckType="2" Name="Check1" Key="Check7" CheckNum="7">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="Nutrition$$C6$$" />
          </Check>
          <Check CheckType="2" Name="Check1" Key="Check8" CheckNum="8">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="Obesity$$C6$$" />
          </Check>
          <Check CheckType="2" Name="Check1" Key="Check9" CheckNum="9">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="Glycemic Control$$C6$$" />
          </Check>
          <Check CheckType="1" Name="Check10" Key="Check10" CheckNum="10">
            <CheckProperty Name="IfCheckPropComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckPropRealComponentID" Value="Cell21" />
            <CheckProperty Name="IfCheckPropProperty" Value="Visible" />
            <CheckProperty Name="IfCheckPropValue" Value="True" />
          </Check>
          <Check CheckType="2" Name="Check11" Key="Check11" CheckNum="11">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="HxofASCVD" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="HxofASCVD" />
            <CheckProperty Name="IfCheckValueOperator" Value="1" />
            <CheckProperty Name="IfCheckValueValue" Value="No$$C6$$" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="4" Name="SimTitle" Key="Action3">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell99" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimTitle" />
          </Action>
          <Action ActionType="4" Name="Risk" Key="Action4">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell22" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="RiskEnhancers" />
          </Action>
          <Action ActionType="4" Name="Action27" Key="Action37">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell28" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimHF" />
          </Action>
          <Action ActionType="4" Name="Action26" Key="Action38">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell27" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimCVA" />
          </Action>
          <Action ActionType="4" Name="Action25" Key="Action39">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell26" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimCHD" />
          </Action>
          <Action ActionType="4" Name="Action25" Key="Action40">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell19" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimASCVd" />
          </Action>
          <Action ActionType="4" Name="Action38" Key="Action41">
            <ActionProperty Name="SetPropertyRealComponentID" Value="per1" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="per1" />
          </Action>
          <Action ActionType="4" Name="Action25" Key="Action42">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell20" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimCVD" />
          </Action>
          <Action ActionType="4" Name="Action38" Key="Action43">
            <ActionProperty Name="SetPropertyRealComponentID" Value="per2" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="per2" />
          </Action>
          <Action ActionType="4" Name="Action38" Key="Action44">
            <ActionProperty Name="SetPropertyRealComponentID" Value="per3" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="per3" />
          </Action>
          <Action ActionType="4" Name="Action38" Key="Action45">
            <ActionProperty Name="SetPropertyRealComponentID" Value="per4" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="per4" />
          </Action>
          <Action ActionType="4" Name="Action38" Key="Action46">
            <ActionProperty Name="SetPropertyRealComponentID" Value="per5" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="per5" />
          </Action>
        </TrueBranch>
        <FalseBranch>
          <Action ActionType="4" Name="SimTitle" Key="Action47">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell99" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimTitle" />
          </Action>
          <Action ActionType="4" Name="Risk" Key="Action48">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell22" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="RiskEnhancers" />
          </Action>
          <Action ActionType="4" Name="Action25" Key="Action49">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell20" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimCVD" />
          </Action>
          <Action ActionType="4" Name="Action25" Key="Action50">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell19" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimASCVd" />
          </Action>
          <Action ActionType="4" Name="Action27" Key="Action51">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell28" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimHF" />
          </Action>
          <Action ActionType="4" Name="Action25" Key="Action52">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell26" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimCHD" />
          </Action>
          <Action ActionType="4" Name="Action26" Key="Action53">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell27" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimCVA" />
          </Action>
          <Action ActionType="4" Name="Action38" Key="Action54">
            <ActionProperty Name="SetPropertyRealComponentID" Value="per1" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="per1" />
          </Action>
          <Action ActionType="4" Name="Action38" Key="Action55">
            <ActionProperty Name="SetPropertyRealComponentID" Value="per2" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="per2" />
          </Action>
          <Action ActionType="4" Name="Action38" Key="Action56">
            <ActionProperty Name="SetPropertyRealComponentID" Value="per3" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="per3" />
          </Action>
          <Action ActionType="4" Name="Action38" Key="Action57">
            <ActionProperty Name="SetPropertyRealComponentID" Value="per4" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="per4" />
          </Action>
          <Action ActionType="4" Name="Action38" Key="Action58">
            <ActionProperty Name="SetPropertyRealComponentID" Value="per5" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="per5" />
          </Action>
        </FalseBranch>
      </Action>
    </Script>
    <Script Name="HxofASCVD_ValueChanged" ProcType="3" CreationType="2" ParamCount="0" Component="">
      <Action ActionType="1" Name="Simulator" Key="Condition1">
        <ActionProperty Name="IfConnectionLogic" Value="1 AND 2" />
        <Checks>
          <Check CheckType="2" Name="Check1" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="HxofASCVD" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="HxofASCVD" />
            <CheckProperty Name="IfCheckValueOperator" Value="1" />
            <CheckProperty Name="IfCheckValueValue" Value="No$$C6$$" />
          </Check>
          <Check CheckType="1" Name="Check2" Key="Check2" CheckNum="2">
            <CheckProperty Name="IfCheckPropComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckPropRealComponentID" Value="Cell21" />
            <CheckProperty Name="IfCheckPropProperty" Value="Visible" />
            <CheckProperty Name="IfCheckPropValue" Value="True" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="4" Name="SimTitle" Key="Action1">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell99" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimTitle" />
          </Action>
          <Action ActionType="4" Name="Risk" Key="Action2">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell22" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="RiskEnhancers" />
          </Action>
          <Action ActionType="4" Name="Action27" Key="Action3">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell28" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimHF" />
          </Action>
          <Action ActionType="4" Name="Action26" Key="Action4">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell27" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimCVA" />
          </Action>
          <Action ActionType="4" Name="Action25" Key="Action5">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell26" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimCHD" />
          </Action>
          <Action ActionType="4" Name="Action25" Key="Action6">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell19" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimASCVd" />
          </Action>
          <Action ActionType="4" Name="Action38" Key="Action7">
            <ActionProperty Name="SetPropertyRealComponentID" Value="per1" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="per1" />
          </Action>
          <Action ActionType="4" Name="Action25" Key="Action8">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell20" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimCVD" />
          </Action>
          <Action ActionType="4" Name="Action38" Key="Action9">
            <ActionProperty Name="SetPropertyRealComponentID" Value="per2" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="per2" />
          </Action>
          <Action ActionType="4" Name="Action38" Key="Action10">
            <ActionProperty Name="SetPropertyRealComponentID" Value="per3" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="per3" />
          </Action>
          <Action ActionType="4" Name="Action38" Key="Action11">
            <ActionProperty Name="SetPropertyRealComponentID" Value="per4" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="per4" />
          </Action>
          <Action ActionType="4" Name="Action38" Key="Action12">
            <ActionProperty Name="SetPropertyRealComponentID" Value="per5" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="per5" />
          </Action>
        </TrueBranch>
        <FalseBranch>
          <Action ActionType="4" Name="SimTitle" Key="Action13">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell99" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimTitle" />
          </Action>
          <Action ActionType="4" Name="Risk" Key="Action14">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell22" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="RiskEnhancers" />
          </Action>
          <Action ActionType="4" Name="Action25" Key="Action15">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell20" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimCVD" />
          </Action>
          <Action ActionType="4" Name="Action25" Key="Action16">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell19" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimASCVd" />
          </Action>
          <Action ActionType="4" Name="Action27" Key="Action17">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell28" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimHF" />
          </Action>
          <Action ActionType="4" Name="Action25" Key="Action18">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell26" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimCHD" />
          </Action>
          <Action ActionType="4" Name="Action26" Key="Action19">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell27" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimCVA" />
          </Action>
          <Action ActionType="4" Name="Action38" Key="Action20">
            <ActionProperty Name="SetPropertyRealComponentID" Value="per1" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="per1" />
          </Action>
          <Action ActionType="4" Name="Action38" Key="Action21">
            <ActionProperty Name="SetPropertyRealComponentID" Value="per2" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="per2" />
          </Action>
          <Action ActionType="4" Name="Action38" Key="Action22">
            <ActionProperty Name="SetPropertyRealComponentID" Value="per3" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="per3" />
          </Action>
          <Action ActionType="4" Name="Action38" Key="Action23">
            <ActionProperty Name="SetPropertyRealComponentID" Value="per4" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="per4" />
          </Action>
          <Action ActionType="4" Name="Action38" Key="Action24">
            <ActionProperty Name="SetPropertyRealComponentID" Value="per5" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="per5" />
          </Action>
        </FalseBranch>
      </Action>
    </Script>
    <Script Name="ModifiableRisk_ValueChanged" ProcType="3" CreationType="2" ParamCount="0" Component="">
      <Action ActionType="1" Name="Simulator" Key="Condition5">
        <ActionProperty Name="IfConnectionLogicType" Value="2" />
        <ActionProperty Name="IfConnectionLogic" Value="(1 OR 2 OR 3 OR 4 OR 5 OR 6 OR 7 OR 8 OR 9) AND 10 AND 11" />
        <Checks>
          <Check CheckType="2" Name="Check1" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="Blood Pressure (goal SBP &lt; 130)$$C6$$" />
          </Check>
          <Check CheckType="2" Name="Check1" Key="Check2" CheckNum="2">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="Cholesterol control$$C6$$" />
          </Check>
          <Check CheckType="2" Name="Check1" Key="Check3" CheckNum="3">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="Smoking counseling$$C6$$" />
          </Check>
          <Check CheckType="2" Name="Check1" Key="Check4" CheckNum="4">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="Alcohol reduction$$C6$$" />
          </Check>
          <Check CheckType="2" Name="Check1" Key="Check5" CheckNum="5">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="Other drug use$$C6$$" />
          </Check>
          <Check CheckType="2" Name="Check1" Key="Check6" CheckNum="6">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="Physical activity$$C6$$" />
          </Check>
          <Check CheckType="2" Name="Check1" Key="Check7" CheckNum="7">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="Nutrition$$C6$$" />
          </Check>
          <Check CheckType="2" Name="Check1" Key="Check8" CheckNum="8">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="Obesity$$C6$$" />
          </Check>
          <Check CheckType="2" Name="Check1" Key="Check9" CheckNum="9">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="Glycemic Control$$C6$$" />
          </Check>
          <Check CheckType="1" Name="Check10" Key="Check10" CheckNum="10">
            <CheckProperty Name="IfCheckPropComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckPropRealComponentID" Value="Cell21" />
            <CheckProperty Name="IfCheckPropProperty" Value="Visible" />
            <CheckProperty Name="IfCheckPropValue" Value="True" />
          </Check>
          <Check CheckType="2" Name="Check11" Key="Check11" CheckNum="11">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="HxofASCVD" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="HxofASCVD" />
            <CheckProperty Name="IfCheckValueOperator" Value="1" />
            <CheckProperty Name="IfCheckValueValue" Value="No$$C6$$" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="4" Name="SimTitle" Key="Action9">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell99" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimTitle" />
          </Action>
          <Action ActionType="4" Name="Risk" Key="Action23">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell22" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="RiskEnhancers" />
          </Action>
          <Action ActionType="4" Name="Action27" Key="Action28">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell28" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimHF" />
          </Action>
          <Action ActionType="4" Name="Action26" Key="Action29">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell27" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimCVA" />
          </Action>
          <Action ActionType="4" Name="Action25" Key="Action30">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell26" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimCHD" />
          </Action>
          <Action ActionType="4" Name="Action25" Key="Action32">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell19" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimASCVd" />
          </Action>
          <Action ActionType="4" Name="Action38" Key="Action38">
            <ActionProperty Name="SetPropertyRealComponentID" Value="per1" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="per1" />
          </Action>
          <Action ActionType="4" Name="Action25" Key="Action31">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell20" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimCVD" />
          </Action>
          <Action ActionType="4" Name="Action38" Key="Action39">
            <ActionProperty Name="SetPropertyRealComponentID" Value="per2" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="per2" />
          </Action>
          <Action ActionType="4" Name="Action38" Key="Action40">
            <ActionProperty Name="SetPropertyRealComponentID" Value="per3" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="per3" />
          </Action>
          <Action ActionType="4" Name="Action38" Key="Action41">
            <ActionProperty Name="SetPropertyRealComponentID" Value="per4" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="per4" />
          </Action>
          <Action ActionType="4" Name="Action38" Key="Action42">
            <ActionProperty Name="SetPropertyRealComponentID" Value="per5" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="per5" />
          </Action>
        </TrueBranch>
        <FalseBranch>
          <Action ActionType="4" Name="SimTitle" Key="Action16">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell99" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimTitle" />
          </Action>
          <Action ActionType="4" Name="Risk" Key="Action24">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell22" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="RiskEnhancers" />
          </Action>
          <Action ActionType="4" Name="Action25" Key="Action25">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell20" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimCVD" />
          </Action>
          <Action ActionType="4" Name="Action25" Key="Action26">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell19" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimASCVd" />
          </Action>
          <Action ActionType="4" Name="Action27" Key="Action27">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell28" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimHF" />
          </Action>
          <Action ActionType="4" Name="Action25" Key="Action33">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell26" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimCHD" />
          </Action>
          <Action ActionType="4" Name="Action26" Key="Action34">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell27" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="SimCVA" />
          </Action>
          <Action ActionType="4" Name="Action38" Key="Action43">
            <ActionProperty Name="SetPropertyRealComponentID" Value="per1" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="per1" />
          </Action>
          <Action ActionType="4" Name="Action38" Key="Action48">
            <ActionProperty Name="SetPropertyRealComponentID" Value="per2" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="per2" />
          </Action>
          <Action ActionType="4" Name="Action38" Key="Action49">
            <ActionProperty Name="SetPropertyRealComponentID" Value="per3" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="per3" />
          </Action>
          <Action ActionType="4" Name="Action38" Key="Action50">
            <ActionProperty Name="SetPropertyRealComponentID" Value="per4" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="per4" />
          </Action>
          <Action ActionType="4" Name="Action38" Key="Action51">
            <ActionProperty Name="SetPropertyRealComponentID" Value="per5" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="per5" />
          </Action>
        </FalseBranch>
      </Action>
      <Action ActionType="1" Name="RiskVis" Key="Condition22">
        <ActionProperty Name="IfConnectionLogic" Value="1" />
        <Checks>
          <Check CheckType="1" Name="Check1" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckPropComponentID" Value="SimCVD" />
            <CheckProperty Name="IfCheckPropRealComponentID" Value="Cell20" />
            <CheckProperty Name="IfCheckPropProperty" Value="Visible" />
            <CheckProperty Name="IfCheckPropValue" Value="True" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="4" Name="Action91" Key="Action91">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell22" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="RiskEnhancers" />
          </Action>
          <Action ActionType="1" Name="PrematureCHD" Key="Condition23">
            <ActionProperty Name="IfConnectionLogic" Value="1" />
            <Checks>
              <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                <CheckProperty Name="IfCheckRuleID" Value="74" />
              </Check>
            </Checks>
            <TrueBranch>
              <Action ActionType="3" Name="Action1" Key="Action61">
                <ActionProperty Name="SetValueRealComponentID" Value="RiskEnhancers" />
                <ActionProperty Name="SetValueOptions" Value="1" />
                <ActionProperty Name="SetValueWhich" Value="1" />
                <ActionProperty Name="SetValueComponentID" Value="RiskEnhancers" />
                <ActionProperty Name="SetValueComponentValue" Value="Family Hx of Premature ASCVD (male &lt; 55 or female &lt; 65)$$C6$$" />
              </Action>
              <Action ActionType="1" Name="CKD" Key="Condition24">
                <ActionProperty Name="IfConnectionLogic" Value="1" />
                <Checks>
                  <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                    <CheckProperty Name="IfCheckRuleID" Value="75" />
                  </Check>
                </Checks>
                <TrueBranch>
                  <Action ActionType="3" Name="Action1" Key="Action62">
                    <ActionProperty Name="SetValueRealComponentID" Value="RiskEnhancers" />
                    <ActionProperty Name="SetValueOptions" Value="1" />
                    <ActionProperty Name="SetValueWhich" Value="1" />
                    <ActionProperty Name="SetValueComponentID" Value="RiskEnhancers" />
                    <ActionProperty Name="SetValueComponentValue" Value="Family Hx of Premature ASCVD (male &lt; 55 or female &lt; 65)$$C5$$CKD 3 to 4 (eGFR 15-59)$$C6$$" />
                  </Action>
                  <Action ActionType="1" Name="Inflam" Key="Condition25">
                    <ActionProperty Name="IfConnectionLogic" Value="1" />
                    <Checks>
                      <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                        <CheckProperty Name="IfCheckRuleID" Value="76" />
                      </Check>
                    </Checks>
                    <TrueBranch>
                      <Action ActionType="3" Name="Action1" Key="Action63">
                        <ActionProperty Name="SetValueRealComponentID" Value="RiskEnhancers" />
                        <ActionProperty Name="SetValueOptions" Value="1" />
                        <ActionProperty Name="SetValueWhich" Value="1" />
                        <ActionProperty Name="SetValueComponentID" Value="RiskEnhancers" />
                        <ActionProperty Name="SetValueComponentValue" Value="Family Hx of Premature ASCVD (male &lt; 55 or female &lt; 65)$$C5$$Chronic inflammatory conditions (RA,Lupus, HIV, or Psoriasis)$$C5$$CKD 3 to 4 (eGFR 15-59)$$C6$$" />
                      </Action>
                      <Action ActionType="1" Name="SA" Key="Condition26">
                        <ActionProperty Name="IfConnectionLogic" Value="1" />
                        <Checks>
                          <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                            <CheckProperty Name="IfCheckRuleID" Value="77" />
                          </Check>
                        </Checks>
                        <TrueBranch>
                          <Action ActionType="3" Name="Action1" Key="Action64">
                            <ActionProperty Name="SetValueRealComponentID" Value="RiskEnhancers" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="RiskEnhancers" />
                            <ActionProperty Name="SetValueComponentValue" Value="Family Hx of Premature ASCVD (male &lt; 55 or female &lt; 65)$$C5$$Chronic inflammatory conditions (RA,Lupus, HIV, or Psoriasis)$$C5$$South Asian Ancestry$$C5$$CKD 3 to 4 (eGFR 15-59)$$C6$$" />
                          </Action>
                        </TrueBranch>
                        <FalseBranch>
                          <Action ActionType="3" Name="Action1" Key="Action65">
                            <ActionProperty Name="SetValueRealComponentID" Value="RiskEnhancers" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="RiskEnhancers" />
                            <ActionProperty Name="SetValueComponentValue" Value="Family Hx of Premature ASCVD (male &lt; 55 or female &lt; 65)$$C5$$Chronic inflammatory conditions (RA,Lupus, HIV, or Psoriasis)$$C5$$CKD 3 to 4 (eGFR 15-59)$$C6$$" />
                          </Action>
                        </FalseBranch>
                      </Action>
                    </TrueBranch>
                    <FalseBranch>
                      <Action ActionType="3" Name="Action1" Key="Action66">
                        <ActionProperty Name="SetValueRealComponentID" Value="RiskEnhancers" />
                        <ActionProperty Name="SetValueOptions" Value="1" />
                        <ActionProperty Name="SetValueWhich" Value="1" />
                        <ActionProperty Name="SetValueComponentID" Value="RiskEnhancers" />
                        <ActionProperty Name="SetValueComponentValue" Value="Family Hx of Premature ASCVD (male &lt; 55 or female &lt; 65)$$C5$$CKD 3 to 4 (eGFR 15-59)$$C6$$" />
                      </Action>
                      <Action ActionType="1" Name="SA" Key="Condition27">
                        <ActionProperty Name="IfConnectionLogic" Value="1" />
                        <Checks>
                          <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                            <CheckProperty Name="IfCheckRuleID" Value="78" />
                          </Check>
                        </Checks>
                        <TrueBranch>
                          <Action ActionType="3" Name="Action1" Key="Action67">
                            <ActionProperty Name="SetValueRealComponentID" Value="RiskEnhancers" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="RiskEnhancers" />
                            <ActionProperty Name="SetValueComponentValue" Value="Family Hx of Premature ASCVD (male &lt; 55 or female &lt; 65)$$C5$$South Asian Ancestry$$C5$$CKD 3 to 4 (eGFR 15-59)$$C6$$" />
                          </Action>
                        </TrueBranch>
                        <FalseBranch>
                          <Action ActionType="3" Name="Action1" Key="Action68">
                            <ActionProperty Name="SetValueRealComponentID" Value="RiskEnhancers" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="RiskEnhancers" />
                            <ActionProperty Name="SetValueComponentValue" Value="Family Hx of Premature ASCVD (male &lt; 55 or female &lt; 65)$$C5$$CKD 3 to 4 (eGFR 15-59)$$C6$$" />
                          </Action>
                        </FalseBranch>
                      </Action>
                    </FalseBranch>
                  </Action>
                </TrueBranch>
                <FalseBranch>
                  <Action ActionType="3" Name="Action1" Key="Action69">
                    <ActionProperty Name="SetValueRealComponentID" Value="RiskEnhancers" />
                    <ActionProperty Name="SetValueOptions" Value="1" />
                    <ActionProperty Name="SetValueWhich" Value="1" />
                    <ActionProperty Name="SetValueComponentID" Value="RiskEnhancers" />
                    <ActionProperty Name="SetValueComponentValue" Value="Family Hx of Premature ASCVD (male &lt; 55 or female &lt; 65)$$C6$$" />
                  </Action>
                  <Action ActionType="1" Name="Inflam" Key="Condition28">
                    <ActionProperty Name="IfConnectionLogic" Value="1" />
                    <Checks>
                      <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                        <CheckProperty Name="IfCheckRuleID" Value="79" />
                      </Check>
                    </Checks>
                    <TrueBranch>
                      <Action ActionType="3" Name="Action1" Key="Action70">
                        <ActionProperty Name="SetValueRealComponentID" Value="RiskEnhancers" />
                        <ActionProperty Name="SetValueOptions" Value="1" />
                        <ActionProperty Name="SetValueWhich" Value="1" />
                        <ActionProperty Name="SetValueComponentID" Value="RiskEnhancers" />
                        <ActionProperty Name="SetValueComponentValue" Value="Family Hx of Premature ASCVD (male &lt; 55 or female &lt; 65)$$C5$$Chronic inflammatory conditions (RA,Lupus, HIV, or Psoriasis)$$C6$$" />
                      </Action>
                      <Action ActionType="1" Name="SA" Key="Condition29">
                        <ActionProperty Name="IfConnectionLogic" Value="1" />
                        <Checks>
                          <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                            <CheckProperty Name="IfCheckRuleID" Value="80" />
                          </Check>
                        </Checks>
                        <TrueBranch>
                          <Action ActionType="3" Name="Action1" Key="Action71">
                            <ActionProperty Name="SetValueRealComponentID" Value="RiskEnhancers" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="RiskEnhancers" />
                            <ActionProperty Name="SetValueComponentValue" Value="Family Hx of Premature ASCVD (male &lt; 55 or female &lt; 65)$$C5$$South Asian Ancestry$$C5$$Chronic inflammatory conditions (RA,Lupus, HIV, or Psoriasis)$$C6$$" />
                          </Action>
                        </TrueBranch>
                        <FalseBranch>
                          <Action ActionType="3" Name="Action1" Key="Action72">
                            <ActionProperty Name="SetValueRealComponentID" Value="RiskEnhancers" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="RiskEnhancers" />
                            <ActionProperty Name="SetValueComponentValue" Value="Family Hx of Premature ASCVD (male &lt; 55 or female &lt; 65)$$C5$$Chronic inflammatory conditions (RA,Lupus, HIV, or Psoriasis)$$C6$$" />
                          </Action>
                        </FalseBranch>
                      </Action>
                    </TrueBranch>
                    <FalseBranch>
                      <Action ActionType="3" Name="Action1" Key="Action73">
                        <ActionProperty Name="SetValueRealComponentID" Value="RiskEnhancers" />
                        <ActionProperty Name="SetValueOptions" Value="1" />
                        <ActionProperty Name="SetValueWhich" Value="1" />
                        <ActionProperty Name="SetValueComponentID" Value="RiskEnhancers" />
                        <ActionProperty Name="SetValueComponentValue" Value="Family Hx of Premature ASCVD (male &lt; 55 or female &lt; 65)$$C6$$" />
                      </Action>
                      <Action ActionType="1" Name="SA" Key="Condition30">
                        <ActionProperty Name="IfConnectionLogic" Value="1" />
                        <Checks>
                          <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                            <CheckProperty Name="IfCheckRuleID" Value="81" />
                          </Check>
                        </Checks>
                        <TrueBranch>
                          <Action ActionType="3" Name="Action1" Key="Action74">
                            <ActionProperty Name="SetValueRealComponentID" Value="RiskEnhancers" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="RiskEnhancers" />
                            <ActionProperty Name="SetValueComponentValue" Value="Family Hx of Premature ASCVD (male &lt; 55 or female &lt; 65)$$C5$$South Asian Ancestry$$C6$$" />
                          </Action>
                        </TrueBranch>
                        <FalseBranch>
                          <Action ActionType="3" Name="Action1" Key="Action75">
                            <ActionProperty Name="SetValueRealComponentID" Value="RiskEnhancers" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="RiskEnhancers" />
                            <ActionProperty Name="SetValueComponentValue" Value="Family Hx of Premature ASCVD (male &lt; 55 or female &lt; 65)$$C6$$" />
                          </Action>
                        </FalseBranch>
                      </Action>
                    </FalseBranch>
                  </Action>
                </FalseBranch>
              </Action>
            </TrueBranch>
            <FalseBranch>
              <Action ActionType="3" Name="Action1" Key="Action76">
                <ActionProperty Name="SetValueRealComponentID" Value="RiskEnhancers" />
                <ActionProperty Name="SetValueOptions" Value="1" />
                <ActionProperty Name="SetValueWhich" Value="1" />
                <ActionProperty Name="SetValueComponentID" Value="RiskEnhancers" />
                <ActionProperty Name="SetValueComponentValue" Value="$$C6$$" />
              </Action>
              <Action ActionType="1" Name="CKD" Key="Condition31">
                <ActionProperty Name="IfConnectionLogic" Value="1" />
                <Checks>
                  <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                    <CheckProperty Name="IfCheckRuleID" Value="82" />
                  </Check>
                </Checks>
                <TrueBranch>
                  <Action ActionType="3" Name="Action1" Key="Action77">
                    <ActionProperty Name="SetValueRealComponentID" Value="RiskEnhancers" />
                    <ActionProperty Name="SetValueOptions" Value="1" />
                    <ActionProperty Name="SetValueWhich" Value="1" />
                    <ActionProperty Name="SetValueComponentID" Value="RiskEnhancers" />
                    <ActionProperty Name="SetValueComponentValue" Value="CKD 3 to 4 (eGFR 15-59)$$C6$$" />
                  </Action>
                  <Action ActionType="1" Name="Inflam" Key="Condition32">
                    <ActionProperty Name="IfConnectionLogic" Value="1" />
                    <Checks>
                      <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                        <CheckProperty Name="IfCheckRuleID" Value="83" />
                      </Check>
                    </Checks>
                    <TrueBranch>
                      <Action ActionType="3" Name="Action1" Key="Action78">
                        <ActionProperty Name="SetValueRealComponentID" Value="RiskEnhancers" />
                        <ActionProperty Name="SetValueOptions" Value="1" />
                        <ActionProperty Name="SetValueWhich" Value="1" />
                        <ActionProperty Name="SetValueComponentID" Value="RiskEnhancers" />
                        <ActionProperty Name="SetValueComponentValue" Value="Chronic inflammatory conditions (RA,Lupus, HIV, or Psoriasis)$$C5$$CKD 3 to 4 (eGFR 15-59)$$C6$$" />
                      </Action>
                      <Action ActionType="1" Name="SA" Key="Condition33">
                        <ActionProperty Name="IfConnectionLogic" Value="1" />
                        <Checks>
                          <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                            <CheckProperty Name="IfCheckRuleID" Value="84" />
                          </Check>
                        </Checks>
                        <TrueBranch>
                          <Action ActionType="3" Name="Action1" Key="Action79">
                            <ActionProperty Name="SetValueRealComponentID" Value="RiskEnhancers" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="RiskEnhancers" />
                            <ActionProperty Name="SetValueComponentValue" Value="South Asian Ancestry$$C5$$Chronic inflammatory conditions (RA,Lupus, HIV, or Psoriasis)$$C5$$CKD 3 to 4 (eGFR 15-59)$$C6$$" />
                          </Action>
                        </TrueBranch>
                        <FalseBranch>
                          <Action ActionType="3" Name="Action1" Key="Action80">
                            <ActionProperty Name="SetValueRealComponentID" Value="RiskEnhancers" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="RiskEnhancers" />
                            <ActionProperty Name="SetValueComponentValue" Value="Chronic inflammatory conditions (RA,Lupus, HIV, or Psoriasis)$$C5$$CKD 3 to 4 (eGFR 15-59)$$C6$$" />
                          </Action>
                        </FalseBranch>
                      </Action>
                    </TrueBranch>
                    <FalseBranch>
                      <Action ActionType="3" Name="Action1" Key="Action81">
                        <ActionProperty Name="SetValueRealComponentID" Value="RiskEnhancers" />
                        <ActionProperty Name="SetValueOptions" Value="1" />
                        <ActionProperty Name="SetValueWhich" Value="1" />
                        <ActionProperty Name="SetValueComponentID" Value="RiskEnhancers" />
                        <ActionProperty Name="SetValueComponentValue" Value="CKD 3 to 4 (eGFR 15-59)$$C6$$" />
                      </Action>
                      <Action ActionType="1" Name="SA" Key="Condition34">
                        <ActionProperty Name="IfConnectionLogic" Value="1" />
                        <Checks>
                          <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                            <CheckProperty Name="IfCheckRuleID" Value="85" />
                          </Check>
                        </Checks>
                        <TrueBranch>
                          <Action ActionType="3" Name="Action1" Key="Action82">
                            <ActionProperty Name="SetValueRealComponentID" Value="RiskEnhancers" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="RiskEnhancers" />
                            <ActionProperty Name="SetValueComponentValue" Value="South Asian Ancestry$$C5$$CKD 3 to 4 (eGFR 15-59)$$C6$$" />
                          </Action>
                        </TrueBranch>
                        <FalseBranch>
                          <Action ActionType="3" Name="Action1" Key="Action83">
                            <ActionProperty Name="SetValueRealComponentID" Value="RiskEnhancers" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="RiskEnhancers" />
                            <ActionProperty Name="SetValueComponentValue" Value="CKD 3 to 4 (eGFR 15-59)$$C6$$" />
                          </Action>
                        </FalseBranch>
                      </Action>
                    </FalseBranch>
                  </Action>
                </TrueBranch>
                <FalseBranch>
                  <Action ActionType="3" Name="Action1" Key="Action84">
                    <ActionProperty Name="SetValueRealComponentID" Value="RiskEnhancers" />
                    <ActionProperty Name="SetValueOptions" Value="1" />
                    <ActionProperty Name="SetValueWhich" Value="1" />
                    <ActionProperty Name="SetValueComponentID" Value="RiskEnhancers" />
                    <ActionProperty Name="SetValueComponentValue" Value="$$C6$$" />
                  </Action>
                  <Action ActionType="1" Name="Inflam" Key="Condition35">
                    <ActionProperty Name="IfConnectionLogic" Value="1" />
                    <Checks>
                      <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                        <CheckProperty Name="IfCheckRuleID" Value="86" />
                      </Check>
                    </Checks>
                    <TrueBranch>
                      <Action ActionType="3" Name="Action1" Key="Action85">
                        <ActionProperty Name="SetValueRealComponentID" Value="RiskEnhancers" />
                        <ActionProperty Name="SetValueOptions" Value="1" />
                        <ActionProperty Name="SetValueWhich" Value="1" />
                        <ActionProperty Name="SetValueComponentID" Value="RiskEnhancers" />
                        <ActionProperty Name="SetValueComponentValue" Value="Chronic inflammatory conditions (RA,Lupus, HIV, or Psoriasis)$$C6$$" />
                      </Action>
                      <Action ActionType="1" Name="SA" Key="Condition36">
                        <ActionProperty Name="IfConnectionLogic" Value="1" />
                        <Checks>
                          <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                            <CheckProperty Name="IfCheckRuleID" Value="87" />
                          </Check>
                        </Checks>
                        <TrueBranch>
                          <Action ActionType="3" Name="Action1" Key="Action86">
                            <ActionProperty Name="SetValueRealComponentID" Value="RiskEnhancers" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="RiskEnhancers" />
                            <ActionProperty Name="SetValueComponentValue" Value="South Asian Ancestry$$C5$$Chronic inflammatory conditions (RA,Lupus, HIV, or Psoriasis)$$C6$$" />
                          </Action>
                        </TrueBranch>
                        <FalseBranch>
                          <Action ActionType="3" Name="Action1" Key="Action87">
                            <ActionProperty Name="SetValueRealComponentID" Value="RiskEnhancers" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="RiskEnhancers" />
                            <ActionProperty Name="SetValueComponentValue" Value="Chronic inflammatory conditions (RA,Lupus, HIV, or Psoriasis)$$C6$$" />
                          </Action>
                        </FalseBranch>
                      </Action>
                    </TrueBranch>
                    <FalseBranch>
                      <Action ActionType="3" Name="Action1" Key="Action88">
                        <ActionProperty Name="SetValueRealComponentID" Value="RiskEnhancers" />
                        <ActionProperty Name="SetValueOptions" Value="1" />
                        <ActionProperty Name="SetValueWhich" Value="1" />
                        <ActionProperty Name="SetValueComponentID" Value="RiskEnhancers" />
                        <ActionProperty Name="SetValueComponentValue" Value="$$C6$$" />
                      </Action>
                      <Action ActionType="1" Name="SA" Key="Condition37">
                        <ActionProperty Name="IfConnectionLogic" Value="1" />
                        <Checks>
                          <Check CheckType="4" Name="Check1" Key="Check1" CheckNum="1">
                            <CheckProperty Name="IfCheckRuleID" Value="88" />
                          </Check>
                        </Checks>
                        <TrueBranch>
                          <Action ActionType="3" Name="Action1" Key="Action89">
                            <ActionProperty Name="SetValueRealComponentID" Value="RiskEnhancers" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="RiskEnhancers" />
                            <ActionProperty Name="SetValueComponentValue" Value="South Asian Ancestry$$C6$$" />
                          </Action>
                        </TrueBranch>
                        <FalseBranch>
                          <Action ActionType="3" Name="Action1" Key="Action90">
                            <ActionProperty Name="SetValueRealComponentID" Value="RiskEnhancers" />
                            <ActionProperty Name="SetValueOptions" Value="1" />
                            <ActionProperty Name="SetValueWhich" Value="1" />
                            <ActionProperty Name="SetValueComponentID" Value="RiskEnhancers" />
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
        </TrueBranch>
        <FalseBranch>
          <Action ActionType="4" Name="Action91" Key="Action93">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell22" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="RiskEnhancers" />
          </Action>
        </FalseBranch>
      </Action>
      <Action ActionType="1" Name="ASCVDRisk" Key="Condition1">
        <ActionProperty Name="IfConnectionLogicType" Value="2" />
        <ActionProperty Name="IfConnectionLogic" Value="(1 OR 2 OR 3 OR 4 OR 5 OR 6 OR 7) AND (8 AND 10 AND 11 AND 9 AND (NOT 12))" />
        <Checks>
          <Check CheckType="2" Name="HxofASCVD" Key="Check8" CheckNum="8">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="HxofASCVD" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="HxofASCVD" />
            <CheckProperty Name="IfCheckValueOperator" Value="1" />
            <CheckProperty Name="IfCheckValueValue" Value="No$$C6$$" />
          </Check>
          <Check CheckType="1" Name="Check10" Key="Check10" CheckNum="10">
            <CheckProperty Name="IfCheckPropComponentID" Value="SimASCVd" />
            <CheckProperty Name="IfCheckPropRealComponentID" Value="Cell19" />
            <CheckProperty Name="IfCheckPropProperty" Value="Visible" />
            <CheckProperty Name="IfCheckPropValue" Value="True" />
          </Check>
          <Check CheckType="1" Name="Check11" Key="Check11" CheckNum="11">
            <CheckProperty Name="IfCheckPropComponentID" Value="RiskEnhancers" />
            <CheckProperty Name="IfCheckPropRealComponentID" Value="Cell22" />
            <CheckProperty Name="IfCheckPropProperty" Value="Visible" />
            <CheckProperty Name="IfCheckPropValue" Value="True" />
          </Check>
          <Check CheckType="4" Name="Check9" Key="Check9" CheckNum="9">
            <CheckProperty Name="IfCheckRuleID" Value="89" />
          </Check>
          <Check CheckType="2" Name="Obesity" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="Obesity$$C6$$" />
          </Check>
          <Check CheckType="2" Name="FamHx" Key="Check2" CheckNum="2">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="Family Hx of CVD$$C6$$" />
          </Check>
          <Check CheckType="2" Name="HTN" Key="Check3" CheckNum="3">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="HTN$$C6$$" />
          </Check>
          <Check CheckType="2" Name="HLD" Key="Check4" CheckNum="4">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="HLD$$C6$$" />
          </Check>
          <Check CheckType="2" Name="TAD" Key="Check5" CheckNum="5">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="Tobacco\Drug\Alcohol$$C6$$" />
          </Check>
          <Check CheckType="2" Name="DM" Key="Check6" CheckNum="6">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="DM$$C6$$" />
          </Check>
          <Check CheckType="2" Name="PreDM" Key="Check7" CheckNum="7">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="DM$$C6$$" />
          </Check>
          <Check CheckType="4" Name="RiskCharge" Key="Check12" CheckNum="12">
            <CheckProperty Name="IfCheckRuleID" Value="90" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="4" Name="Action3" Key="Action4">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell0" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="ASCVDRiskAssessText" />
          </Action>
          <Action ActionType="4" Name="Action14" Key="Action5">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell23" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="ASCVDRiskAssessment" />
          </Action>
        </TrueBranch>
        <FalseBranch>
          <Action ActionType="4" Name="Action14" Key="Action10">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell23" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="ASCVDRiskAssessment" />
          </Action>
          <Action ActionType="4" Name="Action3" Key="Action11">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell0" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="ASCVDRiskAssessText" />
          </Action>
        </FalseBranch>
      </Action>
      <Action ActionType="1" Name="RiskManagement" Key="Condition4">
        <ActionProperty Name="IfConnectionLogicType" Value="2" />
        <ActionProperty Name="IfConnectionLogic" Value="8 AND 10 AND 11 AND 9 AND NOT 1" />
        <Checks>
          <Check CheckType="2" Name="HxofASCVD" Key="Check8" CheckNum="8">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="HxofASCVD" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="HxofASCVD" />
            <CheckProperty Name="IfCheckValueOperator" Value="1" />
            <CheckProperty Name="IfCheckValueValue" Value="No$$C6$$" />
          </Check>
          <Check CheckType="1" Name="Check10" Key="Check10" CheckNum="10">
            <CheckProperty Name="IfCheckPropComponentID" Value="SimASCVd" />
            <CheckProperty Name="IfCheckPropRealComponentID" Value="Cell19" />
            <CheckProperty Name="IfCheckPropProperty" Value="Visible" />
            <CheckProperty Name="IfCheckPropValue" Value="True" />
          </Check>
          <Check CheckType="1" Name="Check11" Key="Check11" CheckNum="11">
            <CheckProperty Name="IfCheckPropComponentID" Value="RiskEnhancers" />
            <CheckProperty Name="IfCheckPropRealComponentID" Value="Cell22" />
            <CheckProperty Name="IfCheckPropProperty" Value="Visible" />
            <CheckProperty Name="IfCheckPropValue" Value="True" />
          </Check>
          <Check CheckType="2" Name="Check9" Key="Check9" CheckNum="9">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="CVD10" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="CVD10" />
            <CheckProperty Name="IfCheckValueOperator" Value="5" />
            <CheckProperty Name="IfCheckValueValue" Value="7.5$$C6$$" />
          </Check>
          <Check CheckType="4" Name="Charge" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckRuleID" Value="91" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="4" Name="Action14" Key="Action3">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell36" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="ASCVDRiskManagement" />
          </Action>
          <Action ActionType="4" Name="Action14" Key="Action6">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell37" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="ASCVDRiskManText" />
          </Action>
        </TrueBranch>
        <FalseBranch>
          <Action ActionType="4" Name="Action14" Key="Action7">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell36" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="ASCVDRiskManagement" />
          </Action>
          <Action ActionType="4" Name="Action14" Key="Action8">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell37" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="ASCVDRiskManText" />
          </Action>
        </FalseBranch>
      </Action>
      <Action ActionType="1" Name="Clear" Key="Condition3">
        <ActionProperty Name="IfConnectionLogicType" Value="1" />
        <ActionProperty Name="IfConnectionLogic" Value="2 OR 1 OR 3 OR 4 OR 5 OR 6 OR 7 OR 8 OR 9 OR 10" />
        <Checks>
          <Check CheckType="2" Name="Check2" Key="Check2" CheckNum="2">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueOperator" Value="8" />
            <CheckProperty Name="IfCheckValueValue" Value="Blood Pressure (goal SBP &lt; 130)$$C6$$" />
          </Check>
          <Check CheckType="2" Name="Check2" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueOperator" Value="8" />
            <CheckProperty Name="IfCheckValueValue" Value="Cholesterol control$$C6$$" />
          </Check>
          <Check CheckType="2" Name="Check2" Key="Check3" CheckNum="3">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueOperator" Value="8" />
            <CheckProperty Name="IfCheckValueValue" Value="Smoking counseling$$C6$$" />
          </Check>
          <Check CheckType="2" Name="Check2" Key="Check4" CheckNum="4">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueOperator" Value="8" />
            <CheckProperty Name="IfCheckValueValue" Value="Alcohol reduction$$C6$$" />
          </Check>
          <Check CheckType="2" Name="Check2" Key="Check5" CheckNum="5">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueOperator" Value="8" />
            <CheckProperty Name="IfCheckValueValue" Value="Other drug use$$C6$$" />
          </Check>
          <Check CheckType="2" Name="Check2" Key="Check6" CheckNum="6">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueOperator" Value="8" />
            <CheckProperty Name="IfCheckValueValue" Value="Physical activity$$C6$$" />
          </Check>
          <Check CheckType="2" Name="Check2" Key="Check7" CheckNum="7">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueOperator" Value="8" />
            <CheckProperty Name="IfCheckValueValue" Value="Nutrition$$C6$$" />
          </Check>
          <Check CheckType="2" Name="Check2" Key="Check8" CheckNum="8">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueOperator" Value="8" />
            <CheckProperty Name="IfCheckValueValue" Value="Obesity$$C6$$" />
          </Check>
          <Check CheckType="2" Name="Check2" Key="Check9" CheckNum="9">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueOperator" Value="8" />
            <CheckProperty Name="IfCheckValueValue" Value="Glycemic Control$$C6$$" />
          </Check>
          <Check CheckType="2" Name="Check2" Key="Check10" CheckNum="10">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueOperator" Value="8" />
            <CheckProperty Name="IfCheckValueValue" Value="None$$C6$$" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="3" Name="Action6" Key="Action97">
            <ActionProperty Name="SetValueRealComponentID" Value="SimDM" />
            <ActionProperty Name="SetValueOptions" Value="1" />
            <ActionProperty Name="SetValueWhich" Value="1" />
            <ActionProperty Name="SetValueComponentID" Value="SimDM" />
            <ActionProperty Name="SetValueComponentValue" Value="$$C6$$" />
          </Action>
          <Action ActionType="3" Name="Action7" Key="Action98">
            <ActionProperty Name="SetValueRealComponentID" Value="SimSM" />
            <ActionProperty Name="SetValueOptions" Value="1" />
            <ActionProperty Name="SetValueWhich" Value="1" />
            <ActionProperty Name="SetValueComponentID" Value="SimSM" />
            <ActionProperty Name="SetValueComponentValue" Value="$$C6$$" />
          </Action>
          <Action ActionType="3" Name="Action8" Key="Action99">
            <ActionProperty Name="SetValueRealComponentID" Value="SimASCVd" />
            <ActionProperty Name="SetValueOptions" Value="1" />
            <ActionProperty Name="SetValueWhich" Value="1" />
            <ActionProperty Name="SetValueComponentID" Value="SimASCVd" />
            <ActionProperty Name="SetValueComponentValue" Value="$$C6$$" />
          </Action>
          <Action ActionType="3" Name="Action9" Key="Action100">
            <ActionProperty Name="SetValueRealComponentID" Value="SimCHD" />
            <ActionProperty Name="SetValueOptions" Value="1" />
            <ActionProperty Name="SetValueWhich" Value="1" />
            <ActionProperty Name="SetValueComponentID" Value="SimCHD" />
            <ActionProperty Name="SetValueComponentValue" Value="$$C6$$" />
          </Action>
          <Action ActionType="3" Name="Action10" Key="Action101">
            <ActionProperty Name="SetValueRealComponentID" Value="SimCVD" />
            <ActionProperty Name="SetValueOptions" Value="1" />
            <ActionProperty Name="SetValueWhich" Value="1" />
            <ActionProperty Name="SetValueComponentID" Value="SimCVD" />
            <ActionProperty Name="SetValueComponentValue" Value="$$C6$$" />
          </Action>
          <Action ActionType="3" Name="Action11" Key="Action102">
            <ActionProperty Name="SetValueRealComponentID" Value="SimCVA" />
            <ActionProperty Name="SetValueOptions" Value="1" />
            <ActionProperty Name="SetValueWhich" Value="1" />
            <ActionProperty Name="SetValueComponentID" Value="SimCVA" />
            <ActionProperty Name="SetValueComponentValue" Value="$$C6$$" />
          </Action>
          <Action ActionType="3" Name="Action12" Key="Action103">
            <ActionProperty Name="SetValueRealComponentID" Value="SimHF" />
            <ActionProperty Name="SetValueOptions" Value="1" />
            <ActionProperty Name="SetValueWhich" Value="1" />
            <ActionProperty Name="SetValueComponentID" Value="SimHF" />
            <ActionProperty Name="SetValueComponentValue" Value="$$C6$$" />
          </Action>
        </TrueBranch>
      </Action>
    </Script>
    <Script Name="ModifiableRisk_ValueChangedNotByLoad" ProcType="3" CreationType="2" ParamCount="0" Component="">
      <Action ActionType="1" Name="Cholesterol" Key="Condition2">
        <ActionProperty Name="IfConnectionLogic" Value="1" />
        <Checks>
          <Check CheckType="2" Name="Check1" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="Cholesterol control$$C6$$" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="3" Name="Action12" Key="Action6">
            <ActionProperty Name="SetValueRealComponentID" Value="SimTC" />
            <ActionProperty Name="SetValueOptions" Value="1" />
            <ActionProperty Name="SetValueWhich" Value="1" />
            <ActionProperty Name="SetValueComponentID" Value="SimTC" />
            <ActionProperty Name="SetValueComponentValue" Value="130$$C6$$" />
          </Action>
          <Action ActionType="3" Name="Action12" Key="Action8">
            <ActionProperty Name="SetValueRealComponentID" Value="SimHDL" />
            <ActionProperty Name="SetValueOptions" Value="1" />
            <ActionProperty Name="SetValueWhich" Value="1" />
            <ActionProperty Name="SetValueComponentID" Value="SimHDL" />
            <ActionProperty Name="SetValueComponentValue" Value="100$$C6$$" />
          </Action>
        </TrueBranch>
        <FalseBranch>
          <Action ActionType="3" Name="Action12" Key="Action10">
            <ActionProperty Name="SetValueRealComponentID" Value="SimTC" />
            <ActionProperty Name="SetValueOptions" Value="1" />
            <ActionProperty Name="SetValueWhich" Value="1" />
            <ActionProperty Name="SetValueComponentID" Value="SimTC" />
            <ActionProperty Name="SetValueComponentValue" Value="$$C6$$" />
          </Action>
          <Action ActionType="3" Name="Action12" Key="Action11">
            <ActionProperty Name="SetValueRealComponentID" Value="SimHDL" />
            <ActionProperty Name="SetValueOptions" Value="1" />
            <ActionProperty Name="SetValueWhich" Value="1" />
            <ActionProperty Name="SetValueComponentID" Value="SimHDL" />
            <ActionProperty Name="SetValueComponentValue" Value="$$C6$$" />
          </Action>
        </FalseBranch>
      </Action>
      <Action ActionType="1" Name="SMCheck" Key="Condition4">
        <ActionProperty Name="IfConnectionLogicType" Value="1" />
        <ActionProperty Name="IfConnectionLogic" Value="1" />
        <Checks>
          <Check CheckType="2" Name="Check1" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="Smoking counseling$$C6$$" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="3" Name="Action17" Key="Action14">
            <ActionProperty Name="SetValueRealComponentID" Value="SimSM" />
            <ActionProperty Name="SetValueOptions" Value="1" />
            <ActionProperty Name="SetValueWhich" Value="1" />
            <ActionProperty Name="SetValueComponentID" Value="SimSM" />
            <ActionProperty Name="SetValueComponentValue" Value="No$$C6$$" />
          </Action>
        </TrueBranch>
        <FalseBranch>
          <Action ActionType="1" Name="Condition6" Key="Condition6">
            <ActionProperty Name="IfConnectionLogic" Value="1" />
            <Checks>
              <Check CheckType="2" Name="Check1" Key="Check1" CheckNum="1">
                <CheckProperty Name="IfCheckValueWhich" Value="1" />
                <CheckProperty Name="IfCheckValueComponentID" Value="Smoker" />
                <CheckProperty Name="IfCheckValueRealComponentID" Value="Smoker" />
                <CheckProperty Name="IfCheckValueOperator" Value="1" />
                <CheckProperty Name="IfCheckValueValue" Value="Yes$$C6$$" />
              </Check>
            </Checks>
            <TrueBranch>
              <Action ActionType="3" Name="Action17" Key="Action15">
                <ActionProperty Name="SetValueRealComponentID" Value="SimSM" />
                <ActionProperty Name="SetValueOptions" Value="1" />
                <ActionProperty Name="SetValueWhich" Value="1" />
                <ActionProperty Name="SetValueComponentID" Value="SimSM" />
                <ActionProperty Name="SetValueComponentValue" Value="Yes$$C6$$" />
              </Action>
            </TrueBranch>
            <FalseBranch>
              <Action ActionType="3" Name="Action17" Key="Action20">
                <ActionProperty Name="SetValueRealComponentID" Value="SimSM" />
                <ActionProperty Name="SetValueOptions" Value="1" />
                <ActionProperty Name="SetValueWhich" Value="1" />
                <ActionProperty Name="SetValueComponentID" Value="SimSM" />
                <ActionProperty Name="SetValueComponentValue" Value="No$$C6$$" />
              </Action>
            </FalseBranch>
          </Action>
        </FalseBranch>
      </Action>
      <Action ActionType="1" Name="DMCheck" Key="Condition5">
        <ActionProperty Name="IfConnectionLogicType" Value="1" />
        <ActionProperty Name="IfConnectionLogic" Value="1" />
        <Checks>
          <Check CheckType="2" Name="Check1" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="ModifiableRisk" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="Glycemic Control$$C6$$" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="3" Name="Action17" Key="Action17">
            <ActionProperty Name="SetValueRealComponentID" Value="SimDM" />
            <ActionProperty Name="SetValueOptions" Value="1" />
            <ActionProperty Name="SetValueWhich" Value="1" />
            <ActionProperty Name="SetValueComponentID" Value="SimDM" />
            <ActionProperty Name="SetValueComponentValue" Value="No$$C6$$" />
          </Action>
        </TrueBranch>
        <FalseBranch>
          <Action ActionType="1" Name="Condition6" Key="Condition7">
            <ActionProperty Name="IfConnectionLogic" Value="1" />
            <Checks>
              <Check CheckType="2" Name="Check1" Key="Check1" CheckNum="1">
                <CheckProperty Name="IfCheckValueWhich" Value="1" />
                <CheckProperty Name="IfCheckValueComponentID" Value="Diabetes" />
                <CheckProperty Name="IfCheckValueRealComponentID" Value="Diabetes" />
                <CheckProperty Name="IfCheckValueOperator" Value="1" />
                <CheckProperty Name="IfCheckValueValue" Value="Yes$$C6$$" />
              </Check>
            </Checks>
            <TrueBranch>
              <Action ActionType="3" Name="Action17" Key="Action21">
                <ActionProperty Name="SetValueRealComponentID" Value="SimDM" />
                <ActionProperty Name="SetValueOptions" Value="1" />
                <ActionProperty Name="SetValueWhich" Value="1" />
                <ActionProperty Name="SetValueComponentID" Value="SimDM" />
                <ActionProperty Name="SetValueComponentValue" Value="Yes$$C6$$" />
              </Action>
            </TrueBranch>
            <FalseBranch>
              <Action ActionType="3" Name="Action17" Key="Action22">
                <ActionProperty Name="SetValueRealComponentID" Value="SimDM" />
                <ActionProperty Name="SetValueOptions" Value="1" />
                <ActionProperty Name="SetValueWhich" Value="1" />
                <ActionProperty Name="SetValueComponentID" Value="SimDM" />
                <ActionProperty Name="SetValueComponentValue" Value="No$$C6$$" />
              </Action>
            </FalseBranch>
          </Action>
        </FalseBranch>
      </Action>
    </Script>
    <Script Name="RiskEnhancers_ValueChanged" ProcType="3" CreationType="2" ParamCount="0" Component="">
      <Action ActionType="1" Name="Cholesterol" Key="Condition3">
        <ActionProperty Name="IfConnectionLogicType" Value="1" />
        <ActionProperty Name="IfConnectionLogic" Value="1 OR 2 OR 3 OR 4" />
        <Checks>
          <Check CheckType="2" Name="Primary HC" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="RiskEnhancers" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="RiskEnhancers" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="Primary hypercholesterolemia (LDL160-189) or (Non-HDL 190-219)$$C6$$" />
          </Check>
          <Check CheckType="2" Name="TGs" Key="Check2" CheckNum="2">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="RiskEnhancers" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="RiskEnhancers" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="Primary Hypertriglyceridemia (&gt;175 mg/dl)$$C6$$" />
          </Check>
          <Check CheckType="2" Name="LipoA" Key="Check3" CheckNum="3">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="RiskEnhancers" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="RiskEnhancers" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="Elevated Lipoprotein(a) (&gt;50 mg/dl)$$C6$$" />
          </Check>
          <Check CheckType="2" Name="LipoB" Key="Check4" CheckNum="4">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="RiskEnhancers" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="RiskEnhancers" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="Elevated apolipoprotein B (&gt;130 mg/dL)$$C6$$" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="4" Name="Action9" Key="Action9">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell6" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="Field0" />
          </Action>
        </TrueBranch>
        <FalseBranch>
          <Action ActionType="4" Name="Action9" Key="Action10">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell6" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="Field0" />
          </Action>
          <Action ActionType="3" Name="Action9" Key="Action12">
            <ActionProperty Name="SetValueRealComponentID" Value="Field0" />
            <ActionProperty Name="SetValueOptions" Value="1" />
            <ActionProperty Name="SetValueWhich" Value="1" />
            <ActionProperty Name="SetValueComponentID" Value="Field0" />
            <ActionProperty Name="SetValueComponentValue" Value="$$C6$$" />
          </Action>
        </FalseBranch>
      </Action>
      <Action ActionType="1" Name="ASCVDRisk" Key="Condition1">
        <ActionProperty Name="IfConnectionLogicType" Value="2" />
        <ActionProperty Name="IfConnectionLogic" Value="(1 OR 2 OR 3 OR 4 OR 5 OR 6 OR 7) AND (8 AND 10 AND 11 AND 9 AND (NOT 12))" />
        <Checks>
          <Check CheckType="2" Name="HxofASCVD" Key="Check8" CheckNum="8">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="HxofASCVD" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="HxofASCVD" />
            <CheckProperty Name="IfCheckValueOperator" Value="1" />
            <CheckProperty Name="IfCheckValueValue" Value="No$$C6$$" />
          </Check>
          <Check CheckType="1" Name="Check10" Key="Check10" CheckNum="10">
            <CheckProperty Name="IfCheckPropComponentID" Value="SimASCVd" />
            <CheckProperty Name="IfCheckPropRealComponentID" Value="Cell19" />
            <CheckProperty Name="IfCheckPropProperty" Value="Visible" />
            <CheckProperty Name="IfCheckPropValue" Value="True" />
          </Check>
          <Check CheckType="1" Name="Check11" Key="Check11" CheckNum="11">
            <CheckProperty Name="IfCheckPropComponentID" Value="RiskEnhancers" />
            <CheckProperty Name="IfCheckPropRealComponentID" Value="Cell22" />
            <CheckProperty Name="IfCheckPropProperty" Value="Visible" />
            <CheckProperty Name="IfCheckPropValue" Value="True" />
          </Check>
          <Check CheckType="4" Name="Check9" Key="Check9" CheckNum="9">
            <CheckProperty Name="IfCheckRuleID" Value="92" />
          </Check>
          <Check CheckType="2" Name="Obesity" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="Obesity$$C6$$" />
          </Check>
          <Check CheckType="2" Name="FamHx" Key="Check2" CheckNum="2">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="Family Hx of CVD$$C6$$" />
          </Check>
          <Check CheckType="2" Name="HTN" Key="Check3" CheckNum="3">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="HTN$$C6$$" />
          </Check>
          <Check CheckType="2" Name="HLD" Key="Check4" CheckNum="4">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="HLD$$C6$$" />
          </Check>
          <Check CheckType="2" Name="TAD" Key="Check5" CheckNum="5">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="Tobacco\Drug\Alcohol$$C6$$" />
          </Check>
          <Check CheckType="2" Name="DM" Key="Check6" CheckNum="6">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="DM$$C6$$" />
          </Check>
          <Check CheckType="2" Name="PreDM" Key="Check7" CheckNum="7">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="Screening" />
            <CheckProperty Name="IfCheckValueOperator" Value="7" />
            <CheckProperty Name="IfCheckValueValue" Value="DM$$C6$$" />
          </Check>
          <Check CheckType="4" Name="RiskCharge" Key="Check12" CheckNum="12">
            <CheckProperty Name="IfCheckRuleID" Value="93" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="4" Name="Action3" Key="Action3">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell0" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="ASCVDRiskAssessText" />
          </Action>
          <Action ActionType="4" Name="Action14" Key="Action1">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell23" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="ASCVDRiskAssessment" />
          </Action>
        </TrueBranch>
        <FalseBranch>
          <Action ActionType="4" Name="Action14" Key="Action2">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell23" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="ASCVDRiskAssessment" />
          </Action>
          <Action ActionType="4" Name="Action3" Key="Action4">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell0" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="ASCVDRiskAssessText" />
          </Action>
        </FalseBranch>
      </Action>
      <Action ActionType="1" Name="RiskManagement" Key="Condition2">
        <ActionProperty Name="IfConnectionLogicType" Value="2" />
        <ActionProperty Name="IfConnectionLogic" Value="8 AND 10 AND 11 AND 9 AND (NOT 1)" />
        <Checks>
          <Check CheckType="2" Name="HxofASCVD" Key="Check8" CheckNum="8">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="HxofASCVD" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="HxofASCVD" />
            <CheckProperty Name="IfCheckValueOperator" Value="1" />
            <CheckProperty Name="IfCheckValueValue" Value="No$$C6$$" />
          </Check>
          <Check CheckType="1" Name="Check10" Key="Check10" CheckNum="10">
            <CheckProperty Name="IfCheckPropComponentID" Value="SimASCVd" />
            <CheckProperty Name="IfCheckPropRealComponentID" Value="Cell19" />
            <CheckProperty Name="IfCheckPropProperty" Value="Visible" />
            <CheckProperty Name="IfCheckPropValue" Value="True" />
          </Check>
          <Check CheckType="1" Name="Check11" Key="Check11" CheckNum="11">
            <CheckProperty Name="IfCheckPropComponentID" Value="RiskEnhancers" />
            <CheckProperty Name="IfCheckPropRealComponentID" Value="Cell22" />
            <CheckProperty Name="IfCheckPropProperty" Value="Visible" />
            <CheckProperty Name="IfCheckPropValue" Value="True" />
          </Check>
          <Check CheckType="2" Name="Check9" Key="Check9" CheckNum="9">
            <CheckProperty Name="IfCheckValueWhich" Value="1" />
            <CheckProperty Name="IfCheckValueComponentID" Value="CVD10" />
            <CheckProperty Name="IfCheckValueRealComponentID" Value="CVD10" />
            <CheckProperty Name="IfCheckValueOperator" Value="5" />
            <CheckProperty Name="IfCheckValueValue" Value="7.5$$C6$$" />
          </Check>
          <Check CheckType="4" Name="ASCVD Risk Management Charge" Key="Check1" CheckNum="1">
            <CheckProperty Name="IfCheckRuleID" Value="94" />
          </Check>
        </Checks>
        <TrueBranch>
          <Action ActionType="4" Name="Action14" Key="Action5">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell36" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="ASCVDRiskManagement" />
          </Action>
          <Action ActionType="4" Name="Action14" Key="Action6">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell37" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="ASCVDRiskManText" />
          </Action>
        </TrueBranch>
        <FalseBranch>
          <Action ActionType="4" Name="Action14" Key="Action7">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell36" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="False" />
            <ActionProperty Name="SetPropertyComponentID" Value="ASCVDRiskManagement" />
          </Action>
          <Action ActionType="4" Name="Action14" Key="Action8">
            <ActionProperty Name="SetPropertyRealComponentID" Value="Cell37" />
            <ActionProperty Name="SetPropertyPropertyName" Value="Visible" />
            <ActionProperty Name="SetPropertyPropertyValue" Value="True" />
            <ActionProperty Name="SetPropertyComponentID" Value="ASCVDRiskManText" />
          </Action>
        </FalseBranch>
      </Action>
    </Script>
  </FormScripts>
</Form>
```
