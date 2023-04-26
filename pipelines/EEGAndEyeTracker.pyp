<?xml version='1.0' encoding='utf-8'?>
<scheme description="" title="EEGAndEyeTracker" version="2.0">
	<nodes>
		<node id="0" name="LSL Input" position="(595.0, 368.0)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="EyeTrackerStream" uuid="48b946bb-5102-4912-9592-c56bbaa745e8" version="1.5.1" />
		<node id="1" name="Select Range" position="(1077.0, 448.0)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" title="Blinking Data" uuid="1f5fd4a4-6b47-4505-98ed-235dbfdb1242" version="1.1.0" />
		<node id="2" name="LSL Input" position="(615.0, 888.0)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="EEG" uuid="80c08671-e35f-4de8-b3f7-af3f26b607a0" version="1.5.1" />
		<node id="3" name="Dejitter Timestamps" position="(815.0, 888.0)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps" uuid="0f127e5e-480f-493f-816d-d7470bb9b638" version="1.0.0" />
		<node id="4" name="Record to XDF" position="(829.0, 528.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF" uuid="847c7840-a7b8-4914-9d98-648bea461c4b" version="1.4.0" />
		<node id="5" name="Record to XDF" position="(715.0, 1088.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF (1)" uuid="36663dcb-2c5f-45fb-bad3-04c331341de6" version="1.4.0" />
		<node id="6" name="Time Series Plot" position="(1243.0, 446.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" title="Time Series Plot (2)" uuid="2ac07903-770a-437b-b821-86c4c995fd0d" version="1.1.0" />
		<node id="7" name="Dejitter Timestamps" position="(825.0, 359.0)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps (2)" uuid="ba6fba06-6dd4-452a-bbd1-33ac0fd32337" version="1.0.0" />
		<node id="8" name="Record to XDF" position="(615.0, 1088.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF (5)" uuid="84a7754e-d9b2-4b7f-84e1-593acc648480" version="1.4.0" />
		<node id="9" name="Record to XDF" position="(729.0, 528.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF (7)" uuid="4987a0d4-4c7e-4184-bfe2-a0a279f441a4" version="1.4.0" />
		<node id="10" name="Constant String" position="(100, 700)" project_name="NeuroPype" qualified_name="widgets.programming.owconstantstring.OWConstantString" title="Constant String" uuid="7a60007b-0dee-4a24-b756-c87cc54bb19f" version="1.0.0" />
		<node id="11" name="IIR Filter" position="(1042.0, 885.0)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owiirfilter.OWIIRFilter" title="IIR Filter (1)" uuid="be7540a9-b2c8-47a7-b02b-fc97d1970d4c" version="1.1.0" />
		<node id="12" name="Record to XDF" position="(1200.0, 883.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF (6)" uuid="d810da39-73a2-4c52-b54b-d99129a90140" version="1.4.0" />
		<node id="13" name="Decimate" position="(932.0, 884.0)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owdecimate.OWDecimate" title="Decimate" uuid="d1704ca9-79cb-4105-b562-3caa4391c403" version="1.0.1" />
		<node id="14" name="Record to XDF" position="(1011.0, 1019.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF (1)" uuid="1be502fb-af73-4c38-bc17-5920f7714f08" version="1.4.0" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="3" source_channel="Data" source_node_id="2" />
		<link enabled="true" id="1" sink_channel="Data" sink_node_id="6" source_channel="Data" source_node_id="1" />
		<link enabled="true" id="2" sink_channel="Data" sink_node_id="7" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="3" sink_channel="Data" sink_node_id="1" source_channel="Data" source_node_id="7" />
		<link enabled="true" id="4" sink_channel="Data" sink_node_id="4" source_channel="Data" source_node_id="7" />
		<link enabled="true" id="5" sink_channel="Data" sink_node_id="5" source_channel="Data" source_node_id="3" />
		<link enabled="true" id="6" sink_channel="Data" sink_node_id="8" source_channel="Data" source_node_id="2" />
		<link enabled="true" id="7" sink_channel="Data" sink_node_id="9" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="8" sink_channel="Output Root" sink_node_id="4" source_channel="Data" source_node_id="10" />
		<link enabled="true" id="9" sink_channel="Output Root" sink_node_id="9" source_channel="Data" source_node_id="10" />
		<link enabled="true" id="10" sink_channel="Output Root" sink_node_id="5" source_channel="Data" source_node_id="10" />
		<link enabled="true" id="11" sink_channel="Output Root" sink_node_id="8" source_channel="Data" source_node_id="10" />
		<link enabled="true" id="12" sink_channel="Output Root" sink_node_id="12" source_channel="Data" source_node_id="10" />
		<link enabled="true" id="13" sink_channel="Data" sink_node_id="12" source_channel="Data" source_node_id="11" />
		<link enabled="true" id="14" sink_channel="Data" sink_node_id="13" source_channel="Data" source_node_id="3" />
		<link enabled="true" id="15" sink_channel="Data" sink_node_id="11" source_channel="Data" source_node_id="13" />
		<link enabled="true" id="16" sink_channel="Data" sink_node_id="14" source_channel="Data" source_node_id="13" />
		<link enabled="true" id="17" sink_channel="Output Root" sink_node_id="14" source_channel="Data" source_node_id="10" />
	</links>
	<annotations>
		<text font-family="Helvetica" font-size="16" id="0" rect="(499.0, 805.0, 244.0, 62.0)">LSL stream for EEG and cleaning up data.</text>
		<text font-family="Helvetica" font-size="16" id="1" rect="(535.0, 247.0, 198.0, 50.0)">LSL stream for eye tracking and blinking.</text>
		<text font-family="Helvetica" font-size="16" id="2" rect="(13.0, 643.0, 252.0, 83.0)">String containing root for recordings</text>
		<text font-family="Helvetica" font-size="16" id="3" rect="(1243.0, 870.0, 340.0, 59.0)">Dejittered + IIR 3rd order, [0.75, 5], EEG</text>
		<text font-family="Helvetica" font-size="16" id="4" rect="(166.0, 1505.0, 367.0, 186.0)">IPDKNOB</text>
	</annotations>
	<thumbnail />
	<node_properties>
		<properties format="pickle" node_id="0">gAN9cQAoWA0AAABjaGFubmVsX25hbWVzcQFdcQJYCgAAAGRhdGFfZHR5cGVxA1gHAAAAZmxvYXQ2
NHEEWAsAAABkaWFnbm9zdGljc3EFiVgTAAAAZXhjbHVkZV9kZXNjX2ZpZWxkc3EGXXEHWA4AAABs
b2NhbGhvc3Rfb25seXEIiVgMAAAAbWFya2VyX3F1ZXJ5cQlYAAAAAHEKWAwAAABtYXhfYmxvY2ts
ZW5xC00ABFgKAAAAbWF4X2J1ZmxlbnEMSx5YDAAAAG1heF9jaHVua2xlbnENSwBYCAAAAG1ldGFk
YXRhcQ59cQ9YDAAAAG5vbWluYWxfcmF0ZXEQWA0AAAAodXNlIGRlZmF1bHQpcRFYCQAAAG9taXRf
ZGVzY3ESiVgPAAAAcHJlYWxsb2NfYnVmZmVycROIWA4AAABwcm9jX2Nsb2Nrc3luY3EUiFgNAAAA
cHJvY19kZWppdHRlcnEViVgPAAAAcHJvY19tb25vdG9uaXplcRaJWA8AAABwcm9jX3RocmVhZHNh
ZmVxF4lYBQAAAHF1ZXJ5cRhYEQAAAG5hbWU9J0V5ZVRyYWNrZXIncRlYBwAAAHJlY292ZXJxGohY
FAAAAHJlc29sdmVfbWluaW11bV90aW1lcRtHP+AAAAAAAABYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0
cnlxHGNzaXAKX3VucGlja2xlX3R5cGUKcR1YDAAAAFB5UXQ1LlF0Q29yZXEeWAoAAABRQnl0ZUFy
cmF5cR9DQgHZ0MsAAwAAAAAGqgAAAoMAAAhEAAAFjwAABqsAAAKwAAAIQwAABY4AAAAAAAAAAA8A
AAAGqwAAArAAAAhDAAAFjnEghXEhh3EiUnEjWA4AAABzZXRfYnJlYWtwb2ludHEkiVgPAAAAdXNl
X3N0cmVhbW5hbWVzcSWJdS4=
</properties>
		<properties format="pickle" node_id="1">gAN9cQAoWBMAAABhcHBseV9tdWx0aXBsZV9heGVzcQGJWB8AAABhcHBseV90aW1lX3NlbGVjdGlv
bl90b19tYXJrZXJzcQKJWAQAAABheGlzcQNYBQAAAHNwYWNlcQRYCAAAAG1ldGFkYXRhcQV9cQZY
EwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxB2NzaXAKX3VucGlja2xlX3R5cGUKcQhYDAAAAFB5UXQ1
LlF0Q29yZXEJWAoAAABRQnl0ZUFycmF5cQpDQgHZ0MsAAwAAAAAKkQAAApcAAA3FAAAFHQAACpIA
AALEAAANxAAABRwAAAAAAAAAAA8AAAAKkgAAAsQAAA3EAAAFHHELhXEMh3ENUnEOWAkAAABzZWxl
Y3Rpb25xD11xEChYCgAAAGxlZnRfYmxpbmtxEVgNAAAAbGVmdF9vcGVubmVzc3ESWAsAAAByaWdo
dF9ibGlua3ETWA4AAAByaWdodF9vcGVubmVzc3EUWAoAAABib3RoX2JsaW5rcRVlWA4AAABzZXRf
YnJlYWtwb2ludHEWiVgEAAAAdW5pdHEXWAUAAABuYW1lc3EYdS4=
</properties>
		<properties format="pickle" node_id="2">gAN9cQAoWA0AAABjaGFubmVsX25hbWVzcQFdcQJYCgAAAGRhdGFfZHR5cGVxA1gHAAAAZmxvYXQ2
NHEEWAsAAABkaWFnbm9zdGljc3EFiVgTAAAAZXhjbHVkZV9kZXNjX2ZpZWxkc3EGXXEHWA4AAABs
b2NhbGhvc3Rfb25seXEIiVgMAAAAbWFya2VyX3F1ZXJ5cQlYAAAAAHEKWAwAAABtYXhfYmxvY2ts
ZW5xC00ABFgKAAAAbWF4X2J1ZmxlbnEMSx5YDAAAAG1heF9jaHVua2xlbnENSwBYCAAAAG1ldGFk
YXRhcQ59cQ9YDAAAAG5vbWluYWxfcmF0ZXEQWA0AAAAodXNlIGRlZmF1bHQpcRFYCQAAAG9taXRf
ZGVzY3ESiVgPAAAAcHJlYWxsb2NfYnVmZmVycROIWA4AAABwcm9jX2Nsb2Nrc3luY3EUiFgNAAAA
cHJvY19kZWppdHRlcnEViVgPAAAAcHJvY19tb25vdG9uaXplcRaJWA8AAABwcm9jX3RocmVhZHNh
ZmVxF4lYBQAAAHF1ZXJ5cRhYHAAAAG5hbWU9J0xpdmVBbXBTTi0wNTYzMDktMDU1MydxGVgHAAAA
cmVjb3ZlcnEaiFgUAAAAcmVzb2x2ZV9taW5pbXVtX3RpbWVxG0c/4AAAAAAAAFgTAAAAc2F2ZWRX
aWRnZXRHZW9tZXRyeXEcY3NpcApfdW5waWNrbGVfdHlwZQpxHVgMAAAAUHlRdDUuUXRDb3JlcR5Y
CgAAAFFCeXRlQXJyYXlxH0NCAdnQywADAAAAAAarAAACsAAACEMAAAWOAAAGqwAAArAAAAhDAAAF
jgAAAAAAAAAADwAAAAarAAACsAAACEMAAAWOcSCFcSGHcSJScSNYDgAAAHNldF9icmVha3BvaW50
cSSJWA8AAAB1c2Vfc3RyZWFtbmFtZXNxJYl1Lg==
</properties>
		<properties format="literal" node_id="3">{'force_monotonic': True, 'forget_halftime': 90, 'max_updaterate': 500, 'metadata': {}, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'warmup_samples': -1}</properties>
		<properties format="pickle" node_id="4">gAN9cQAoWAwAAABhbGxvd19kb3VibGVxAYlYDwAAAGNsb3NlX29uX21hcmtlcnECWA8AAABjbG9z
ZS1yZWNvcmRpbmdxA1gNAAAAY2xvdWRfYWNjb3VudHEEWAAAAABxBVgMAAAAY2xvdWRfYnVja2V0
cQZoBVgRAAAAY2xvdWRfY3JlZGVudGlhbHNxB2gFWAoAAABjbG91ZF9ob3N0cQhYBwAAAERlZmF1
bHRxCVgOAAAAY2xvdWRfcGFydHNpemVxCkseWAwAAABkZWxldGVfcGFydHNxC4hYCAAAAGZpbGVu
YW1lcQxYIAAAAGRlaml0dGVyZWQtZ2F6ZS1hbmQtYmxpbmtpbmcueGRmcQ1YCAAAAG1ldGFkYXRh
cQ59cQ9YCwAAAG91dHB1dF9yb290cRBoBVgaAAAAcHJlc2VydmVfb3JpZ2luYWxfbWV0YWRhdGFx
EYlYCwAAAHJldHJpZXZhYmxlcRKJWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cRNjc2lwCl91bnBp
Y2tsZV90eXBlCnEUWAwAAABQeVF0NS5RdENvcmVxFVgKAAAAUUJ5dGVBcnJheXEWQ0IB2dDLAAMA
AAAABsIAAALWAAAIKwAABTsAAAbDAAADAwAACCoAAAU6AAAAAAAAAAAPAAAABsMAAAMDAAAIKgAA
BTpxF4VxGIdxGVJxGlgNAAAAc2Vzc2lvbl9ub3Rlc3EbaAVYDgAAAHNldF9icmVha3BvaW50cRyJ
WAcAAAB2ZXJib3NlcR2JdS4=
</properties>
		<properties format="pickle" node_id="5">gAN9cQAoWAwAAABhbGxvd19kb3VibGVxAYlYDwAAAGNsb3NlX29uX21hcmtlcnECWA8AAABjbG9z
ZS1yZWNvcmRpbmdxA1gNAAAAY2xvdWRfYWNjb3VudHEEWAAAAABxBVgMAAAAY2xvdWRfYnVja2V0
cQZoBVgRAAAAY2xvdWRfY3JlZGVudGlhbHNxB2gFWAoAAABjbG91ZF9ob3N0cQhYBwAAAERlZmF1
bHRxCVgOAAAAY2xvdWRfcGFydHNpemVxCkseWAwAAABkZWxldGVfcGFydHNxC4hYCAAAAGZpbGVu
YW1lcQxYEgAAAGRlaml0dGVyZWQtZWVnLnhkZnENWAgAAABtZXRhZGF0YXEOfXEPWAsAAABvdXRw
dXRfcm9vdHEQaAVYGgAAAHByZXNlcnZlX29yaWdpbmFsX21ldGFkYXRhcRGJWAsAAAByZXRyaWV2
YWJsZXESiVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXETY3NpcApfdW5waWNrbGVfdHlwZQpxFFgM
AAAAUHlRdDUuUXRDb3JlcRVYCgAAAFFCeXRlQXJyYXlxFkNCAdnQywADAAAAAAbCAAAC1gAACCsA
AAU7AAAGwwAAAwMAAAgqAAAFOgAAAAAAAAAADwAAAAbDAAADAwAACCoAAAU6cReFcRiHcRlScRpY
DQAAAHNlc3Npb25fbm90ZXNxG2gFWA4AAABzZXRfYnJlYWtwb2ludHEciVgHAAAAdmVyYm9zZXEd
iXUu
</properties>
		<properties format="pickle" node_id="6">gAN9cQAoWA0AAABhYnNvbHV0ZV90aW1lcQGIWA0AAABhbHdheXNfb25fdG9wcQKJWAsAAABhbnRp
YWxpYXNlZHEDiFgQAAAAYXV0b19saW5lX2NvbG9yc3EEiFgJAAAAYXV0b3NjYWxlcQWJWBAAAABi
YWNrZ3JvdW5kX2NvbG9ycQZYBwAAACNGRkZGRkZxB1gQAAAAZGVjb3JhdGlvbl9jb2xvcnEIWAcA
AAAjMDAwMDAwcQlYCwAAAGRvd25zYW1wbGVkcQqJWAkAAABmb250X3NpemVxC0dAJAAAAAAAAFgM
AAAAaW5pdGlhbF9kaW1zcQxdcQ0oSzJLMk28Ak30AWVYCgAAAGxpbmVfY29sb3JxDlgHAAAAIzAw
MDAwMHEPWAoAAABsaW5lX3dpZHRocRBHP+gAAAAAAABYDAAAAG1hcmtlcl9jb2xvcnERWAcAAAAj
RkYwMDAwcRJYDAAAAG1heF9jaGFubmVsc3ETSyBYCAAAAG1ldGFkYXRhcRR9cRVYDAAAAG5hbnNf
YXNfemVyb3EWiFgOAAAAbm9fY29uY2F0ZW5hdGVxF4lYDgAAAG92ZXJyaWRlX3NyYXRlcRhYDQAA
ACh1c2UgZGVmYXVsdClxGVgMAAAAcGxvdF9tYXJrZXJzcRqIWAsAAABwbG90X21pbm1heHEbiVgT
AAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEcY3NpcApfdW5waWNrbGVfdHlwZQpxHVgMAAAAUHlRdDUu
UXRDb3JlcR5YCgAAAFFCeXRlQXJyYXlxH0NCAdnQywADAAAAAAbuAAACMQAACGYAAAX2AAAG7wAA
Al4AAAhlAAAF9QAAAAAAAAAADwAAAAbvAAACXgAACGUAAAX1cSCFcSGHcSJScSNYBQAAAHNjYWxl
cSRHP+gAAAAAAABYDgAAAHNldF9icmVha3BvaW50cSWJWAwAAABzaG93X3Rvb2xiYXJxJolYCwAA
AHN0cmVhbV9uYW1lcSdYDQAAACh1c2UgZGVmYXVsdClxKFgKAAAAdGltZV9yYW5nZXEpR0AkAAAA
AAAAWAUAAAB0aXRsZXEqWBAAAABUaW1lIHNlcmllcyB2aWV3cStYCgAAAHplcm9fY29sb3JxLFgH
AAAAIzdGN0Y3RnEtWAgAAAB6ZXJvbWVhbnEuiXUu
</properties>
		<properties format="pickle" node_id="7">gAN9cQAoWA8AAABmb3JjZV9tb25vdG9uaWNxAYhYDwAAAGZvcmdldF9oYWxmdGltZXECS1pYDgAA
AG1heF91cGRhdGVyYXRlcQNN9AFYCAAAAG1ldGFkYXRhcQR9cQVYEwAAAHNhdmVkV2lkZ2V0R2Vv
bWV0cnlxBmNzaXAKX3VucGlja2xlX3R5cGUKcQdYDAAAAFB5UXQ1LlF0Q29yZXEIWAoAAABRQnl0
ZUFycmF5cQlDQgHZ0MsAAwAAAAAGqgAAA2sAAAhEAAAEpwAABqsAAAOYAAAIQwAABKYAAAAAAAAA
AA8AAAAGqwAAA5gAAAhDAAAEpnEKhXELh3EMUnENWA4AAABzZXRfYnJlYWtwb2ludHEOiVgOAAAA
d2FybXVwX3NhbXBsZXNxD0r/////dS4=
</properties>
		<properties format="pickle" node_id="8">gAN9cQAoWAwAAABhbGxvd19kb3VibGVxAYlYDwAAAGNsb3NlX29uX21hcmtlcnECWA8AAABjbG9z
ZS1yZWNvcmRpbmdxA1gNAAAAY2xvdWRfYWNjb3VudHEEWAAAAABxBVgMAAAAY2xvdWRfYnVja2V0
cQZoBVgRAAAAY2xvdWRfY3JlZGVudGlhbHNxB2gFWAoAAABjbG91ZF9ob3N0cQhYBwAAAERlZmF1
bHRxCVgOAAAAY2xvdWRfcGFydHNpemVxCkseWAwAAABkZWxldGVfcGFydHNxC4hYCAAAAGZpbGVu
YW1lcQxYCwAAAHJhdy1lZWcueGRmcQ1YCAAAAG1ldGFkYXRhcQ59cQ9YCwAAAG91dHB1dF9yb290
cRBoBVgaAAAAcHJlc2VydmVfb3JpZ2luYWxfbWV0YWRhdGFxEYlYCwAAAHJldHJpZXZhYmxlcRKJ
WBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cRNjc2lwCl91bnBpY2tsZV90eXBlCnEUWAwAAABQeVF0
NS5RdENvcmVxFVgKAAAAUUJ5dGVBcnJheXEWQ0IB2dDLAAMAAAAABsIAAALWAAAIKwAABTsAAAbD
AAADAwAACCoAAAU6AAAAAAAAAAAPAAAABsMAAAMDAAAIKgAABTpxF4VxGIdxGVJxGlgNAAAAc2Vz
c2lvbl9ub3Rlc3EbaAVYDgAAAHNldF9icmVha3BvaW50cRyJWAcAAAB2ZXJib3NlcR2JdS4=
</properties>
		<properties format="pickle" node_id="9">gAN9cQAoWAwAAABhbGxvd19kb3VibGVxAYlYDwAAAGNsb3NlX29uX21hcmtlcnECWA8AAABjbG9z
ZS1yZWNvcmRpbmdxA1gNAAAAY2xvdWRfYWNjb3VudHEEWAAAAABxBVgMAAAAY2xvdWRfYnVja2V0
cQZoBVgRAAAAY2xvdWRfY3JlZGVudGlhbHNxB2gFWAoAAABjbG91ZF9ob3N0cQhYBwAAAERlZmF1
bHRxCVgOAAAAY2xvdWRfcGFydHNpemVxCkseWAwAAABkZWxldGVfcGFydHNxC4hYCAAAAGZpbGVu
YW1lcQxYFQAAAGdhemUtYW5kLWJsaW5raW5nLnhkZnENWAgAAABtZXRhZGF0YXEOfXEPWAsAAABv
dXRwdXRfcm9vdHEQaAVYGgAAAHByZXNlcnZlX29yaWdpbmFsX21ldGFkYXRhcRGJWAsAAAByZXRy
aWV2YWJsZXESiVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXETY3NpcApfdW5waWNrbGVfdHlwZQpx
FFgMAAAAUHlRdDUuUXRDb3JlcRVYCgAAAFFCeXRlQXJyYXlxFkNCAdnQywADAAAAAAbCAAAC1gAA
CCsAAAU7AAAGwwAAAwMAAAgqAAAFOgAAAAAAAAAADwAAAAbDAAADAwAACCoAAAU6cReFcRiHcRlS
cRpYDQAAAHNlc3Npb25fbm90ZXNxG2gFWA4AAABzZXRfYnJlYWtwb2ludHEciVgHAAAAdmVyYm9z
ZXEdiXUu
</properties>
		<properties format="pickle" node_id="10">gAN9cQAoWAgAAABtZXRhZGF0YXEBfXECWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQNjc2lwCl91
bnBpY2tsZV90eXBlCnEEWAwAAABQeVF0NS5RdENvcmVxBVgKAAAAUUJ5dGVBcnJheXEGQ0IB2dDL
AAMAAAAABsMAAAPFAAAJlQAABHgAAAbDAAADxQAACZUAAAR4AAAAAAAAAAAPAAAABsMAAAPFAAAJ
lQAABHhxB4VxCIdxCVJxClgOAAAAc2V0X2JyZWFrcG9pbnRxC4lYBQAAAHZhbHVlcQxYPgAAAEM6
L1VzZXJzL3ZpemxhYl9zdHVkL2lkYXR0MjkwMF9ncjkyL25ldXJvcHlwZS1waXBlbGluZS9MU0xE
YXRhcQ11Lg==
</properties>
		<properties format="pickle" node_id="11">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgGAAAAZGVzaWducQNYBgAAAGJ1dHRlcnEEWAsA
AABmcmVxdWVuY2llc3EFXXEGKEc/6AAAAAAAAEsFZVgLAAAAaWdub3JlX25hbnNxB4lYCAAAAG1l
dGFkYXRhcQh9cQlYBAAAAG1vZGVxClgIAAAAYmFuZHBhc3NxC1gQAAAAb2ZmbGluZV9maWx0Zmls
dHEMiVgFAAAAb3JkZXJxDUsDWAkAAABwYXNzX2xvc3NxDkdACAAAAAAAAFgTAAAAc2F2ZWRXaWRn
ZXRHZW9tZXRyeXEPY3NpcApfdW5waWNrbGVfdHlwZQpxEFgMAAAAUHlRdDUuUXRDb3JlcRFYCgAA
AFFCeXRlQXJyYXlxEkNCAdnQywADAAAAAAawAAADIgAACD0AAATwAAAGsQAAA08AAAg8AAAE7wAA
AAAAAAAADwAAAAaxAAADTwAACDwAAATvcROFcRSHcRVScRZYDgAAAHNldF9icmVha3BvaW50cReJ
WAoAAABzdG9wX2F0dGVucRhHQEkAAAAAAAB1Lg==
</properties>
		<properties format="pickle" node_id="12">gAN9cQAoWAwAAABhbGxvd19kb3VibGVxAYlYDwAAAGNsb3NlX29uX21hcmtlcnECWA8AAABjbG9z
ZS1yZWNvcmRpbmdxA1gNAAAAY2xvdWRfYWNjb3VudHEEWAAAAABxBVgMAAAAY2xvdWRfYnVja2V0
cQZoBVgRAAAAY2xvdWRfY3JlZGVudGlhbHNxB2gFWAoAAABjbG91ZF9ob3N0cQhYBwAAAERlZmF1
bHRxCVgOAAAAY2xvdWRfcGFydHNpemVxCkseWAwAAABkZWxldGVfcGFydHNxC4hYCAAAAGZpbGVu
YW1lcQxYJQAAAGRlaml0dGVyZWQtaWlyLTNvcmRlci0wLjc1dG81LWVlZy54ZGZxDVgIAAAAbWV0
YWRhdGFxDn1xD1gLAAAAb3V0cHV0X3Jvb3RxEGgFWBoAAABwcmVzZXJ2ZV9vcmlnaW5hbF9tZXRh
ZGF0YXERiVgLAAAAcmV0cmlldmFibGVxEolYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxE2NzaXAK
X3VucGlja2xlX3R5cGUKcRRYDAAAAFB5UXQ1LlF0Q29yZXEVWAoAAABRQnl0ZUFycmF5cRZDQgHZ
0MsAAwAAAAAGwgAAAtYAAAmPAAAFOwAABsMAAAMDAAAJjgAABToAAAAAAAAAAA8AAAAGwwAAAwMA
AAmOAAAFOnEXhXEYh3EZUnEaWA0AAABzZXNzaW9uX25vdGVzcRtoBVgOAAAAc2V0X2JyZWFrcG9p
bnRxHIlYBwAAAHZlcmJvc2VxHYl1Lg==
</properties>
		<properties format="pickle" node_id="13">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgGAAAAZmFjdG9ycQNLAlgIAAAAbWV0YWRhdGFx
BH1xBVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEGY3NpcApfdW5waWNrbGVfdHlwZQpxB1gMAAAA
UHlRdDUuUXRDb3JlcQhYCgAAAFFCeXRlQXJyYXlxCUNCAdnQywADAAAAAAbCAAADigAACCsAAASI
AAAGwwAAA7cAAAgqAAAEhwAAAAAAAAAADwAAAAbDAAADtwAACCoAAASHcQqFcQuHcQxScQ1YDgAA
AHNldF9icmVha3BvaW50cQ6JdS4=
</properties>
		<properties format="pickle" node_id="14">gAN9cQAoWAwAAABhbGxvd19kb3VibGVxAYlYDwAAAGNsb3NlX29uX21hcmtlcnECWA8AAABjbG9z
ZS1yZWNvcmRpbmdxA1gNAAAAY2xvdWRfYWNjb3VudHEEWAAAAABxBVgMAAAAY2xvdWRfYnVja2V0
cQZoBVgRAAAAY2xvdWRfY3JlZGVudGlhbHNxB2gFWAoAAABjbG91ZF9ob3N0cQhYBwAAAERlZmF1
bHRxCVgOAAAAY2xvdWRfcGFydHNpemVxCkseWAwAAABkZWxldGVfcGFydHNxC4hYCAAAAGZpbGVu
YW1lcQxYHAAAAGRlY2ltYXRlZC1kZWppdHRlcmVkLWVlZy54ZGZxDVgIAAAAbWV0YWRhdGFxDn1x
D1gLAAAAb3V0cHV0X3Jvb3RxEGgFWBoAAABwcmVzZXJ2ZV9vcmlnaW5hbF9tZXRhZGF0YXERiVgL
AAAAcmV0cmlldmFibGVxEolYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxE2NzaXAKX3VucGlja2xl
X3R5cGUKcRRYDAAAAFB5UXQ1LlF0Q29yZXEVWAoAAABRQnl0ZUFycmF5cRZDQgHZ0MsAAwAAAAAG
wgAAAtYAAAgrAAAFOwAABsMAAAMDAAAIKgAABToAAAAAAAAAAA8AAAAGwwAAAwMAAAgqAAAFOnEX
hXEYh3EZUnEaWA0AAABzZXNzaW9uX25vdGVzcRtoBVgOAAAAc2V0X2JyZWFrcG9pbnRxHIlYBwAA
AHZlcmJvc2VxHYl1Lg==
</properties>
	</node_properties>
	<patch>{
    "description": {
        "description": "(description missing)",
        "license": "",
        "name": "(untitled)",
        "status": "(unspecified)",
        "url": "",
        "version": "0.0.0"
    },
    "edges": [
        [
            "node3",
            "data",
            "node4",
            "data"
        ],
        [
            "node3",
            "data",
            "node9",
            "data"
        ],
        [
            "node2",
            "data",
            "node7",
            "data"
        ],
        [
            "node1",
            "data",
            "node8",
            "data"
        ],
        [
            "node1",
            "data",
            "node10",
            "data"
        ],
        [
            "node8",
            "data",
            "node2",
            "data"
        ],
        [
            "node8",
            "data",
            "node5",
            "data"
        ],
        [
            "node4",
            "data",
            "node6",
            "data"
        ],
        [
            "node4",
            "data",
            "node14",
            "data"
        ],
        [
            "node11",
            "data",
            "node5",
            "output_root"
        ],
        [
            "node11",
            "data",
            "node10",
            "output_root"
        ],
        [
            "node11",
            "data",
            "node6",
            "output_root"
        ],
        [
            "node11",
            "data",
            "node9",
            "output_root"
        ],
        [
            "node11",
            "data",
            "node13",
            "output_root"
        ],
        [
            "node11",
            "data",
            "node15",
            "output_root"
        ],
        [
            "node12",
            "data",
            "node13",
            "data"
        ],
        [
            "node14",
            "data",
            "node12",
            "data"
        ],
        [
            "node14",
            "data",
            "node15",
            "data"
        ]
    ],
    "nodes": {
        "node1": {
            "class": "LSLInput",
            "module": "neuropype.nodes.network.LSLInput",
            "params": {
                "channel_names": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "data_dtype": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "float64"
                },
                "diagnostics": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "exclude_desc_fields": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "localhost_only": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_query": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "max_blocklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1024
                },
                "max_buflen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
                },
                "max_chunklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "nominal_rate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "omit_desc": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "prealloc_buffer": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "proc_clocksync": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "proc_dejitter": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "proc_monotonize": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "proc_threadsafe": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "query": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "name='EyeTracker'"
                },
                "recover": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "resolve_minimum_time": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.5
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "use_streamnames": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "48b946bb-5102-4912-9592-c56bbaa745e8"
        },
        "node10": {
            "class": "RecordToXDF",
            "module": "neuropype.nodes.file_system.RecordToXDF",
            "params": {
                "allow_double": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "close_on_marker": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "close-recording"
                },
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "cloud_partsize": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
                },
                "delete_parts": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "gaze-and-blinking.xdf"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "output_root": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "preserve_original_metadata": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "retrievable": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "session_notes": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "4987a0d4-4c7e-4184-bfe2-a0a279f441a4"
        },
        "node11": {
            "class": "ConstantString",
            "module": "neuropype.nodes.programming.ConstantString",
            "params": {
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "value": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "C:/Users/vizlab_stud/idatt2900_gr92/neuropype-pipeline/LSLData"
                }
            },
            "uuid": "7a60007b-0dee-4a24-b756-c87cc54bb19f"
        },
        "node12": {
            "class": "IIRFilter",
            "module": "neuropype.nodes.signal_processing.IIRFilter",
            "params": {
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "time"
                },
                "design": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "butter"
                },
                "frequencies": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        0.75,
                        5
                    ]
                },
                "ignore_nans": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "mode": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "bandpass"
                },
                "offline_filtfilt": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "order": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 3
                },
                "pass_loss": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 3.0
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stop_atten": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 50.0
                }
            },
            "uuid": "be7540a9-b2c8-47a7-b02b-fc97d1970d4c"
        },
        "node13": {
            "class": "RecordToXDF",
            "module": "neuropype.nodes.file_system.RecordToXDF",
            "params": {
                "allow_double": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "close_on_marker": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "close-recording"
                },
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "cloud_partsize": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
                },
                "delete_parts": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "dejittered-iir-3order-0.75to5-eeg.xdf"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "output_root": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "preserve_original_metadata": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "retrievable": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "session_notes": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "d810da39-73a2-4c52-b54b-d99129a90140"
        },
        "node14": {
            "class": "Decimate",
            "module": "neuropype.nodes.signal_processing.Decimate",
            "params": {
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "time"
                },
                "factor": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 2
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "d1704ca9-79cb-4105-b562-3caa4391c403"
        },
        "node15": {
            "class": "RecordToXDF",
            "module": "neuropype.nodes.file_system.RecordToXDF",
            "params": {
                "allow_double": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "close_on_marker": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "close-recording"
                },
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "cloud_partsize": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
                },
                "delete_parts": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "decimated-dejittered-eeg.xdf"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "output_root": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "preserve_original_metadata": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "retrievable": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "session_notes": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "1be502fb-af73-4c38-bc17-5920f7714f08"
        },
        "node2": {
            "class": "SelectRange",
            "module": "neuropype.nodes.tensor_math.SelectRange",
            "params": {
                "apply_multiple_axes": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "apply_time_selection_to_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "space"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "selection": {
                    "customized": true,
                    "type": "Port",
                    "value": [
                        "left_blink",
                        "left_openness",
                        "right_blink",
                        "right_openness",
                        "both_blink"
                    ]
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "unit": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "names"
                }
            },
            "uuid": "1f5fd4a4-6b47-4505-98ed-235dbfdb1242"
        },
        "node3": {
            "class": "LSLInput",
            "module": "neuropype.nodes.network.LSLInput",
            "params": {
                "channel_names": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "data_dtype": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "float64"
                },
                "diagnostics": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "exclude_desc_fields": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "localhost_only": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_query": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "max_blocklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1024
                },
                "max_buflen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
                },
                "max_chunklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "nominal_rate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "omit_desc": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "prealloc_buffer": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "proc_clocksync": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "proc_dejitter": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "proc_monotonize": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "proc_threadsafe": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "query": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "name='LiveAmpSN-056309-0553'"
                },
                "recover": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "resolve_minimum_time": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.5
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "use_streamnames": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "80c08671-e35f-4de8-b3f7-af3f26b607a0"
        },
        "node4": {
            "class": "DejitterTimestamps",
            "module": "neuropype.nodes.utilities.DejitterTimestamps",
            "params": {
                "force_monotonic": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "forget_halftime": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 90
                },
                "max_updaterate": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 500
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "warmup_samples": {
                    "customized": false,
                    "type": "IntPort",
                    "value": -1
                }
            },
            "uuid": "0f127e5e-480f-493f-816d-d7470bb9b638"
        },
        "node5": {
            "class": "RecordToXDF",
            "module": "neuropype.nodes.file_system.RecordToXDF",
            "params": {
                "allow_double": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "close_on_marker": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "close-recording"
                },
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "cloud_partsize": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
                },
                "delete_parts": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "dejittered-gaze-and-blinking.xdf"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "output_root": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "preserve_original_metadata": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "retrievable": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "session_notes": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "847c7840-a7b8-4914-9d98-648bea461c4b"
        },
        "node6": {
            "class": "RecordToXDF",
            "module": "neuropype.nodes.file_system.RecordToXDF",
            "params": {
                "allow_double": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "close_on_marker": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "close-recording"
                },
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "cloud_partsize": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
                },
                "delete_parts": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "dejittered-eeg.xdf"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "output_root": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "preserve_original_metadata": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "retrievable": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "session_notes": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "36663dcb-2c5f-45fb-bad3-04c331341de6"
        },
        "node7": {
            "class": "TimeSeriesPlot",
            "module": "neuropype.nodes.visualization.TimeSeriesPlot",
            "params": {
                "absolute_time": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "antialiased": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "auto_line_colors": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "autoscale": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
                },
                "background_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#FFFFFF"
                },
                "decoration_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "downsampled": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "font_size": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 10.0
                },
                "initial_dims": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        50,
                        50,
                        700,
                        500
                    ]
                },
                "line_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "line_width": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.75
                },
                "marker_color": {
                    "customized": false,
                    "type": "Port",
                    "value": "#FF0000"
                },
                "max_channels": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 32
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "nans_as_zero": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "no_concatenate": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "override_srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "plot_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "plot_minmax": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "scale": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 0.75
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "show_toolbar": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "time_range": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 10.0
                },
                "title": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Time series view"
                },
                "zero_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#7F7F7F"
                },
                "zeromean": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "2ac07903-770a-437b-b821-86c4c995fd0d"
        },
        "node8": {
            "class": "DejitterTimestamps",
            "module": "neuropype.nodes.utilities.DejitterTimestamps",
            "params": {
                "force_monotonic": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "forget_halftime": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 90
                },
                "max_updaterate": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 500
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "warmup_samples": {
                    "customized": false,
                    "type": "IntPort",
                    "value": -1
                }
            },
            "uuid": "ba6fba06-6dd4-452a-bbd1-33ac0fd32337"
        },
        "node9": {
            "class": "RecordToXDF",
            "module": "neuropype.nodes.file_system.RecordToXDF",
            "params": {
                "allow_double": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "close_on_marker": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "close-recording"
                },
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "cloud_partsize": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
                },
                "delete_parts": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "raw-eeg.xdf"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "output_root": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "preserve_original_metadata": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "retrievable": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "session_notes": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "84a7754e-d9b2-4b7f-84e1-593acc648480"
        }
    },
    "version": 1.1
}</patch>
</scheme>
