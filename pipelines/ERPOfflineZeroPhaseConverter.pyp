<?xml version='1.0' encoding='utf-8'?>
<scheme description="" title="ERPOfflineZeroPhaseConverter" version="2.0">
	<nodes>
		<node id="0" name="Record to XDF" position="(1344.0, 840.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF" uuid="1b1c8b70-60c3-42b3-80ff-7baf2c9f7529" version="1.4.0" />
		<node id="1" name="Stream Data" position="(981.0, 554.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owstreamdata.OWStreamData" title="Stream Data (3)" uuid="fa111a4d-63ac-4e2a-850f-9133849d8491" version="1.3.0" />
		<node id="2" name="Dejitter Timestamps" position="(629.0, 551.0)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps (3)" uuid="82647279-931a-49fa-88ff-9218d8b90db3" version="1.0.0" />
		<node id="3" name="Fuse Streams" position="(1240.0, 456.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owfusestreams.OWFuseStreams" title="Fuse Streams (1)" uuid="5614d095-09c2-45ba-b244-d789837e7359" version="0.9.6" />
		<node id="4" name="Stream Data" position="(980.0, 423.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owstreamdata.OWStreamData" title="Stream Data (4)" uuid="98b2ba1c-99f7-49a2-a8c8-e224ad82e6b2" version="1.3.0" />
		<node id="5" name="Fuse Streams" position="(1183.0, 826.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owfusestreams.OWFuseStreams" title="Fuse Streams (1)" uuid="55d3288d-4f98-4c89-ad1a-e529f5a1d366" version="0.9.6" />
		<node id="6" name="Record to XDF" position="(1400.0, 471.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF" uuid="f4f62075-6f01-4645-9657-afcc7bac336b" version="1.4.0" />
		<node id="7" name="Dejitter Timestamps" position="(711.0, 415.0)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps" uuid="a87cd633-27d1-40b7-abfc-1de148e49914" version="1.0.0" />
		<node id="8" name="Merge Streams" position="(1057.0, 808.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owmergestreams.OWMergeStreams" title="Merge Streams (2)" uuid="32d56b91-a58f-451d-9299-2461b90d5c4b" version="1.0.0" />
		<node id="9" name="Import XDF" position="(575.0, 432.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportxdf.OWImportXDF" title="Import XDF (2)" uuid="29ee8052-0944-4af5-9c0b-4fd9c7d11fa1" version="1.4.2" />
		<node id="10" name="Import XDF" position="(501.0, 541.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportxdf.OWImportXDF" title="Import XDF" uuid="e16fe69e-fc54-47fa-adb4-f51a2e7862a1" version="1.4.2" />
		<node id="11" name="Merge Streams" position="(1114.0, 438.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owmergestreams.OWMergeStreams" title="Merge Streams (2)" uuid="8d343c29-6b6e-4e0d-b9b4-8a71ca5d8335" version="1.0.0" />
		<node id="12" name="IIR Filter" position="(840.0, 508.0)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owiirfilter.OWIIRFilter" title="IIR Filter (3)" uuid="d5ca0e90-d3fd-40e7-adec-db0b722e2529" version="1.1.0" />
		<node id="13" name="Time Series Plot" position="(919.0, 305.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" title="Time Series Plot (1)" uuid="702cbd9e-9163-4c9c-ba14-3a82f57535f2" version="1.1.0" />
		<node id="14" name="Stream Data" position="(953.0, 906.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owstreamdata.OWStreamData" title="Stream Data (3)" uuid="9a679611-4af4-4fb0-877e-425e3be205f2" version="1.3.0" />
		<node id="15" name="IIR Filter" position="(839.0, 669.0)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owiirfilter.OWIIRFilter" title="IIR Filter (3)" uuid="3140d8e9-d35b-41e6-a0d5-8e50e9335571" version="1.1.0" />
		<node id="16" name="Constant String" position="(1536.0, 646.0)" project_name="NeuroPype" qualified_name="widgets.programming.owconstantstring.OWConstantString" title="Constant String" uuid="70d04b47-8c05-417b-8b37-15c584fe3679" version="1.0.0" />
		<node id="17" name="Shift Timestamps" position="(751.0, 561.0)" project_name="NeuroPype" qualified_name="widgets.utilities.owshifttimestamps.OWShiftTimestamps" title="Shift Timestamps" uuid="02074e53-f041-4a35-ba59-e5ace492f09c" version="1.2.1" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="0" source_channel="Data" source_node_id="5" />
		<link enabled="true" id="1" sink_channel="Output Root" sink_node_id="0" source_channel="Data" source_node_id="16" />
		<link enabled="true" id="2" sink_channel="Data" sink_node_id="1" source_channel="Data" source_node_id="12" />
		<link enabled="true" id="3" sink_channel="Data2" sink_node_id="11" source_channel="Data" source_node_id="1" />
		<link enabled="true" id="4" sink_channel="Data" sink_node_id="2" source_channel="Data" source_node_id="10" />
		<link enabled="true" id="5" sink_channel="Data" sink_node_id="3" source_channel="Outdata" source_node_id="11" />
		<link enabled="true" id="6" sink_channel="Data" sink_node_id="6" source_channel="Data" source_node_id="3" />
		<link enabled="true" id="7" sink_channel="Data" sink_node_id="4" source_channel="Data" source_node_id="7" />
		<link enabled="true" id="8" sink_channel="Data1" sink_node_id="8" source_channel="Data" source_node_id="4" />
		<link enabled="true" id="9" sink_channel="Data" sink_node_id="13" source_channel="Data" source_node_id="4" />
		<link enabled="true" id="10" sink_channel="Data1" sink_node_id="11" source_channel="Data" source_node_id="4" />
		<link enabled="true" id="11" sink_channel="Data" sink_node_id="5" source_channel="Outdata" source_node_id="8" />
		<link enabled="true" id="12" sink_channel="Output Root" sink_node_id="6" source_channel="Data" source_node_id="16" />
		<link enabled="true" id="13" sink_channel="Data" sink_node_id="7" source_channel="Data" source_node_id="9" />
		<link enabled="true" id="14" sink_channel="Data2" sink_node_id="8" source_channel="Data" source_node_id="14" />
		<link enabled="true" id="15" sink_channel="Data" sink_node_id="14" source_channel="Data" source_node_id="15" />
		<link enabled="true" id="16" sink_channel="Data" sink_node_id="17" source_channel="Data" source_node_id="2" />
		<link enabled="true" id="17" sink_channel="Data" sink_node_id="12" source_channel="Data" source_node_id="17" />
		<link enabled="true" id="18" sink_channel="Data" sink_node_id="15" source_channel="Data" source_node_id="17" />
	</links>
	<annotations>
		<text font-family="Helvetica" font-size="16" id="0" rect="(1045.0, 287.0, 353.0, 80.0)">Merging dejittered + timestampshifted 43ms  + [12,27] + 4th order + offline filtfilt IIR and dejittered eye tracker</text>
		<text font-family="Helvetica" font-size="16" id="1" rect="(1076.0, 693.0, 345.0, 66.0)">Merging dejittered  + timestampshifted 43ms + [12, 70] + 4th order + offline filtfilt IIR and dejittered eye tracker</text>
	</annotations>
	<thumbnail />
	<node_properties>
		<properties format="pickle" node_id="0">gAN9cQAoWAwAAABhbGxvd19kb3VibGVxAYlYDwAAAGNsb3NlX29uX21hcmtlcnECWA8AAABjbG9z
ZS1yZWNvcmRpbmdxA1gNAAAAY2xvdWRfYWNjb3VudHEEWAAAAABxBVgMAAAAY2xvdWRfYnVja2V0
cQZoBVgRAAAAY2xvdWRfY3JlZGVudGlhbHNxB2gFWAoAAABjbG91ZF9ob3N0cQhYBwAAAERlZmF1
bHRxCVgOAAAAY2xvdWRfcGFydHNpemVxCkseWAwAAABkZWxldGVfcGFydHNxC4hYCAAAAGZpbGVu
YW1lcQxYawAAAHplcm9waGFzZS1kZWppdHRlcmVkLXNoaWZ0ZWQ0M21zcG9zaXRpdmUtaWlyLTRv
cmRlci0xMnRvNzAtZWVnLWFuZC1kZWppdHRlcmVkLXVuaXR5LWZyZXF1ZW5jaWVzLVlmb3JtYXQu
eGRmcQ1YCAAAAG1ldGFkYXRhcQ59cQ9YCwAAAG91dHB1dF9yb290cRBoBVgaAAAAcHJlc2VydmVf
b3JpZ2luYWxfbWV0YWRhdGFxEYlYCwAAAHJldHJpZXZhYmxlcRKJWBMAAABzYXZlZFdpZGdldEdl
b21ldHJ5cRNjc2lwCl91bnBpY2tsZV90eXBlCnEUWAwAAABQeVF0NS5RdENvcmVxFVgKAAAAUUJ5
dGVBcnJheXEWQ0IB2dDLAAMAAAAABsIAAALWAAAKlwAABTsAAAbDAAADAwAACpYAAAU6AAAAAAAA
AAAPAAAABsMAAAMDAAAKlgAABTpxF4VxGIdxGVJxGlgNAAAAc2Vzc2lvbl9ub3Rlc3EbaAVYDgAA
AHNldF9icmVha3BvaW50cRyJWAcAAAB2ZXJib3NlcR2JdS4=
</properties>
		<properties format="pickle" node_id="1">gAN9cQAoWAoAAABkYXRhX2R0eXBlcQFYBwAAAGZsb2F0NjRxAlgUAAAAZGF0YV9yYW5nZV90b19z
dHJlYW1xA1gLAAAAbGVnYWN5LXdhcm5xBFgRAAAAaGl0Y2hfcHJvYmFiaWxpdHlxBUcAAAAAAAAA
AFgOAAAAaml0dGVyX3BlcmNlbnRxBksFWAwAAABsb2dfcHJvZ3Jlc3NxB4lYBwAAAGxvb3Bpbmdx
CIlYCAAAAG1ldGFkYXRhcQl9cQpYCAAAAHJhbmRzZWVkcQtN54ZYEwAAAHNhdmVkV2lkZ2V0R2Vv
bWV0cnlxDGNzaXAKX3VucGlja2xlX3R5cGUKcQ1YDAAAAFB5UXQ1LlF0Q29yZXEOWAoAAABRQnl0
ZUFycmF5cQ9DQgHZ0MsAAwAAAAAGfQAAAvIAAAhwAAAFIAAABn4AAAMfAAAIbwAABR8AAAAAAAAA
AA8AAAAGfgAAAx8AAAhvAAAFH3EQhXERh3ESUnETWA4AAABzZXRfYnJlYWtwb2ludHEUiVgHAAAA
c3BlZWR1cHEVRz/wAAAAAAAAWAkAAABzdGFydF9wb3NxFkcAAAAAAAAAAFgQAAAAdGltZXN0YW1w
X2ppdHRlcnEXRwAAAAAAAAAAWAYAAAB0aW1pbmdxGFgJAAAAd2FsbGNsb2NrcRlYDwAAAHVwZGF0
ZV9pbnRlcnZhbHEaRz+keuFHrhR7dS4=
</properties>
		<properties format="literal" node_id="2">{'force_monotonic': True, 'forget_halftime': 90, 'max_updaterate': 500, 'metadata': {}, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'warmup_samples': -1}</properties>
		<properties format="pickle" node_id="3">gAN9cQAoWAwAAABidWZmZXJfZGVsYXlxAUsCWBAAAABkZXNpcmVkX2hlYWRyb29tcQJLBVgIAAAA
bWV0YWRhdGFxA31xBFgMAAAAbWluX2hlYWRyb29tcQVLAlgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRy
eXEGY3NpcApfdW5waWNrbGVfdHlwZQpxB1gMAAAAUHlRdDUuUXRDb3JlcQhYCgAAAFFCeXRlQXJy
YXlxCUNCAdnQywADAAAAAAavAAADSAAACD4AAATJAAAGsAAAA3UAAAg9AAAEyAAAAAAAAAAADwAA
AAawAAADdQAACD0AAATIcQqFcQuHcQxScQ1YDgAAAHNldF9icmVha3BvaW50cQ6JWAUAAABzcmF0
ZXEPS/pYCwAAAHN0cmVhbV9uYW1lcRBYAwAAAGVlZ3ERWAkAAAB2ZXJib3NpdHlxEksBdS4=
</properties>
		<properties format="pickle" node_id="4">gAN9cQAoWAoAAABkYXRhX2R0eXBlcQFYBwAAAGZsb2F0NjRxAlgUAAAAZGF0YV9yYW5nZV90b19z
dHJlYW1xA1gLAAAAbGVnYWN5LXdhcm5xBFgRAAAAaGl0Y2hfcHJvYmFiaWxpdHlxBUcAAAAAAAAA
AFgOAAAAaml0dGVyX3BlcmNlbnRxBksFWAwAAABsb2dfcHJvZ3Jlc3NxB4lYBwAAAGxvb3Bpbmdx
CIlYCAAAAG1ldGFkYXRhcQl9cQpYCAAAAHJhbmRzZWVkcQtN54ZYEwAAAHNhdmVkV2lkZ2V0R2Vv
bWV0cnlxDGNzaXAKX3VucGlja2xlX3R5cGUKcQ1YDAAAAFB5UXQ1LlF0Q29yZXEOWAoAAABRQnl0
ZUFycmF5cQ9DQgHZ0MsAAwAAAAAGfQAAAvIAAAhwAAAFIAAABn4AAAMfAAAIbwAABR8AAAAAAAAA
AA8AAAAGfgAAAx8AAAhvAAAFH3EQhXERh3ESUnETWA4AAABzZXRfYnJlYWtwb2ludHEUiVgHAAAA
c3BlZWR1cHEVRz/wAAAAAAAAWAkAAABzdGFydF9wb3NxFkcAAAAAAAAAAFgQAAAAdGltZXN0YW1w
X2ppdHRlcnEXRwAAAAAAAAAAWAYAAAB0aW1pbmdxGFgJAAAAd2FsbGNsb2NrcRlYDwAAAHVwZGF0
ZV9pbnRlcnZhbHEaRz+keuFHrhR7dS4=
</properties>
		<properties format="pickle" node_id="5">gAN9cQAoWAwAAABidWZmZXJfZGVsYXlxAUsCWBAAAABkZXNpcmVkX2hlYWRyb29tcQJLBVgIAAAA
bWV0YWRhdGFxA31xBFgMAAAAbWluX2hlYWRyb29tcQVLAlgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRy
eXEGY3NpcApfdW5waWNrbGVfdHlwZQpxB1gMAAAAUHlRdDUuUXRDb3JlcQhYCgAAAFFCeXRlQXJy
YXlxCUNCAdnQywADAAAAAAavAAADSAAACD4AAATJAAAGsAAAA3UAAAg9AAAEyAAAAAAAAAAADwAA
AAawAAADdQAACD0AAATIcQqFcQuHcQxScQ1YDgAAAHNldF9icmVha3BvaW50cQ6JWAUAAABzcmF0
ZXEPS/pYCwAAAHN0cmVhbV9uYW1lcRBYAwAAAGVlZ3ERWAkAAAB2ZXJib3NpdHlxEksBdS4=
</properties>
		<properties format="pickle" node_id="6">gAN9cQAoWAwAAABhbGxvd19kb3VibGVxAYlYDwAAAGNsb3NlX29uX21hcmtlcnECWA8AAABjbG9z
ZS1yZWNvcmRpbmdxA1gNAAAAY2xvdWRfYWNjb3VudHEEWAAAAABxBVgMAAAAY2xvdWRfYnVja2V0
cQZoBVgRAAAAY2xvdWRfY3JlZGVudGlhbHNxB2gFWAoAAABjbG91ZF9ob3N0cQhYBwAAAERlZmF1
bHRxCVgOAAAAY2xvdWRfcGFydHNpemVxCkseWAwAAABkZWxldGVfcGFydHNxC4hYCAAAAGZpbGVu
YW1lcQxYawAAAHplcm9waGFzZS1kZWppdHRlcmVkLXNoaWZ0ZWQ0M21zcG9zaXRpdmUtaWlyLTRv
cmRlci0xMnRvMjctZWVnLWFuZC1kZWppdHRlcmVkLXVuaXR5LWZyZXF1ZW5jaWVzLVlmb3JtYXQu
eGRmcQ1YCAAAAG1ldGFkYXRhcQ59cQ9YCwAAAG91dHB1dF9yb290cRBoBVgaAAAAcHJlc2VydmVf
b3JpZ2luYWxfbWV0YWRhdGFxEYlYCwAAAHJldHJpZXZhYmxlcRKJWBMAAABzYXZlZFdpZGdldEdl
b21ldHJ5cRNjc2lwCl91bnBpY2tsZV90eXBlCnEUWAwAAABQeVF0NS5RdENvcmVxFVgKAAAAUUJ5
dGVBcnJheXEWQ0IB2dDLAAMAAAAABsIAAALWAAAK4wAABTsAAAbDAAADAwAACuIAAAU6AAAAAAAA
AAAPAAAABsMAAAMDAAAK4gAABTpxF4VxGIdxGVJxGlgNAAAAc2Vzc2lvbl9ub3Rlc3EbaAVYDgAA
AHNldF9icmVha3BvaW50cRyJWAcAAAB2ZXJib3NlcR2JdS4=
</properties>
		<properties format="pickle" node_id="7">gAN9cQAoWA8AAABmb3JjZV9tb25vdG9uaWNxAYhYDwAAAGZvcmdldF9oYWxmdGltZXECS1pYDgAA
AG1heF91cGRhdGVyYXRlcQNN9AFYCAAAAG1ldGFkYXRhcQR9cQVYEwAAAHNhdmVkV2lkZ2V0R2Vv
bWV0cnlxBmNzaXAKX3VucGlja2xlX3R5cGUKcQdYDAAAAFB5UXQ1LlF0Q29yZXEIWAoAAABRQnl0
ZUFycmF5cQlDQgHZ0MsAAwAAAAAGqgAAA2sAAAhEAAAEpwAABqsAAAOYAAAIQwAABKYAAAAAAAAA
AA8AAAAGqwAAA5gAAAhDAAAEpnEKhXELh3EMUnENWA4AAABzZXRfYnJlYWtwb2ludHEOiVgOAAAA
d2FybXVwX3NhbXBsZXNxD0r/////dS4=
</properties>
		<properties format="pickle" node_id="8">gAN9cQAoWAgAAABtZXRhZGF0YXEBfXECWBEAAAByZXBsYWNlX2lmX2V4aXN0c3EDiVgTAAAAc2F2
ZWRXaWRnZXRHZW9tZXRyeXEEY3NpcApfdW5waWNrbGVfdHlwZQpxBVgMAAAAUHlRdDUuUXRDb3Jl
cQZYCgAAAFFCeXRlQXJyYXlxB0NCAdnQywADAAAAAAbCAAADjAAACCsAAASFAAAGwwAAA7kAAAgq
AAAEhAAAAAAAAAAADwAAAAbDAAADuQAACCoAAASEcQiFcQmHcQpScQtYDgAAAHNldF9icmVha3Bv
aW50cQyJWAcAAABzb3J0aW5ncQ1YBQAAAGlucHV0cQ51Lg==
</properties>
		<properties format="pickle" node_id="9">gAN9cQAoWA0AAABjbG91ZF9hY2NvdW50cQFYAAAAAHECWAwAAABjbG91ZF9idWNrZXRxA2gCWBEA
AABjbG91ZF9jcmVkZW50aWFsc3EEaAJYCgAAAGNsb3VkX2hvc3RxBVgHAAAARGVmYXVsdHEGWAgA
AABmaWxlbmFtZXEHWIEAAABDOi9Vc2Vycy92aXpsYWJfc3R1ZC9pZGF0dDI5MDBfZ3I5Mi9uZXVy
b3B5cGUtcGlwZWxpbmUvQkNJU3BlbGxlclY4L0JDSVNwZWxsZXJfQV81X3RpbWVzL2Rlaml0dGVy
ZWQtdW5pdHktZnJlcXVlbmNpZXMtWWZvcm1hdC54ZGZxCFgTAAAAaGFuZGxlX2Nsb2NrX3Jlc2V0
c3EJiFgRAAAAaGFuZGxlX2Nsb2NrX3N5bmNxCohYFQAAAGhhbmRsZV9qaXR0ZXJfcmVtb3ZhbHEL
iFgOAAAAbWF4X21hcmtlcl9sZW5xDFgNAAAAKHVzZSBkZWZhdWx0KXENWAgAAABtZXRhZGF0YXEO
fXEPWBIAAAByZW9yZGVyX3RpbWVzdGFtcHNxEIlYDgAAAHJldGFpbl9zdHJlYW1zcRFYDQAAACh1
c2UgZGVmYXVsdClxElgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXETY3NpcApfdW5waWNrbGVfdHlw
ZQpxFFgMAAAAUHlRdDUuUXRDb3JlcRVYCgAAAFFCeXRlQXJyYXlxFkNCAdnQywADAAAAAAbCAAAC
2wAACzUAAAU2AAAGwwAAAwgAAAs0AAAFNQAAAAAAAAAADwAAAAbDAAADCAAACzQAAAU1cReFcRiH
cRlScRpYDgAAAHNldF9icmVha3BvaW50cRuJWAsAAAB1c2VfY2FjaGluZ3EciVgPAAAAdXNlX3N0
cmVhbW5hbWVzcR2IWAcAAAB2ZXJib3NlcR6JdS4=
</properties>
		<properties format="pickle" node_id="10">gAN9cQAoWA0AAABjbG91ZF9hY2NvdW50cQFYAAAAAHECWAwAAABjbG91ZF9idWNrZXRxA2gCWBEA
AABjbG91ZF9jcmVkZW50aWFsc3EEaAJYCgAAAGNsb3VkX2hvc3RxBVgHAAAARGVmYXVsdHEGWAgA
AABmaWxlbmFtZXEHWGsAAABDOi9Vc2Vycy92aXpsYWJfc3R1ZC9pZGF0dDI5MDBfZ3I5Mi9uZXVy
b3B5cGUtcGlwZWxpbmUvQkNJU3BlbGxlclY4L0JDSVNwZWxsZXJfQV81X3RpbWVzL2Rlaml0dGVy
ZWQtZWVnLnhkZnEIWBMAAABoYW5kbGVfY2xvY2tfcmVzZXRzcQmIWBEAAABoYW5kbGVfY2xvY2tf
c3luY3EKiFgVAAAAaGFuZGxlX2ppdHRlcl9yZW1vdmFscQuIWA4AAABtYXhfbWFya2VyX2xlbnEM
WA0AAAAodXNlIGRlZmF1bHQpcQ1YCAAAAG1ldGFkYXRhcQ59cQ9YEgAAAHJlb3JkZXJfdGltZXN0
YW1wc3EQiVgOAAAAcmV0YWluX3N0cmVhbXNxEVgNAAAAKHVzZSBkZWZhdWx0KXESWBMAAABzYXZl
ZFdpZGdldEdlb21ldHJ5cRNjc2lwCl91bnBpY2tsZV90eXBlCnEUWAwAAABQeVF0NS5RdENvcmVx
FVgKAAAAUUJ5dGVBcnJheXEWQ0IB2dDLAAMAAAAABsIAAALbAAALAgAABTYAAAbDAAADCAAACwEA
AAU1AAAAAAAAAAAPAAAABsMAAAMIAAALAQAABTVxF4VxGIdxGVJxGlgOAAAAc2V0X2JyZWFrcG9p
bnRxG4lYCwAAAHVzZV9jYWNoaW5ncRyJWA8AAAB1c2Vfc3RyZWFtbmFtZXNxHYhYBwAAAHZlcmJv
c2VxHol1Lg==
</properties>
		<properties format="literal" node_id="11">{'metadata': {}, 'replace_if_exists': False, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'sorting': 'input'}</properties>
		<properties format="pickle" node_id="12">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgGAAAAZGVzaWducQNYBgAAAGJ1dHRlcnEEWAsA
AABmcmVxdWVuY2llc3EFXXEGKEsMSxtlWAsAAABpZ25vcmVfbmFuc3EHiVgIAAAAbWV0YWRhdGFx
CH1xCVgEAAAAbW9kZXEKWAgAAABiYW5kcGFzc3ELWBAAAABvZmZsaW5lX2ZpbHRmaWx0cQyIWAUA
AABvcmRlcnENSwRYCQAAAHBhc3NfbG9zc3EOR0AIAAAAAAAAWBMAAABzYXZlZFdpZGdldEdlb21l
dHJ5cQ9jc2lwCl91bnBpY2tsZV90eXBlCnEQWAwAAABQeVF0NS5RdENvcmVxEVgKAAAAUUJ5dGVB
cnJheXESQ0IB2dDLAAMAAAAABVAAAAMIAAAG3QAABNYAAAVRAAADNQAABtwAAATVAAAAAAAAAAAP
AAAABVEAAAM1AAAG3AAABNVxE4VxFIdxFVJxFlgOAAAAc2V0X2JyZWFrcG9pbnRxF4lYCgAAAHN0
b3BfYXR0ZW5xGEdASQAAAAAAAHUu
</properties>
		<properties format="literal" node_id="13">{'absolute_time': False, 'always_on_top': False, 'antialiased': True, 'auto_line_colors': False, 'autoscale': True, 'background_color': '#FFFFFF', 'decoration_color': '#000000', 'downsampled': False, 'font_size': 10.0, 'initial_dims': [50, 50, 700, 500], 'line_color': '#000000', 'line_width': 0.75, 'marker_color': '#FF0000', 'max_channels': 32, 'metadata': {}, 'nans_as_zero': False, 'no_concatenate': False, 'override_srate': '(use default)', 'plot_markers': True, 'plot_minmax': False, 'savedWidgetGeometry': None, 'scale': 1.0, 'set_breakpoint': False, 'show_toolbar': False, 'stream_name': '(use default)', 'time_range': 5.0, 'title': 'Time series view', 'zero_color': '#7F7F7F', 'zeromean': True}</properties>
		<properties format="pickle" node_id="14">gAN9cQAoWAoAAABkYXRhX2R0eXBlcQFYBwAAAGZsb2F0NjRxAlgUAAAAZGF0YV9yYW5nZV90b19z
dHJlYW1xA1gLAAAAbGVnYWN5LXdhcm5xBFgRAAAAaGl0Y2hfcHJvYmFiaWxpdHlxBUcAAAAAAAAA
AFgOAAAAaml0dGVyX3BlcmNlbnRxBksFWAwAAABsb2dfcHJvZ3Jlc3NxB4lYBwAAAGxvb3Bpbmdx
CIlYCAAAAG1ldGFkYXRhcQl9cQpYCAAAAHJhbmRzZWVkcQtN54ZYEwAAAHNhdmVkV2lkZ2V0R2Vv
bWV0cnlxDGNzaXAKX3VucGlja2xlX3R5cGUKcQ1YDAAAAFB5UXQ1LlF0Q29yZXEOWAoAAABRQnl0
ZUFycmF5cQ9DQgHZ0MsAAwAAAAAGfQAAAvIAAAhwAAAFIAAABn4AAAMfAAAIbwAABR8AAAAAAAAA
AA8AAAAGfgAAAx8AAAhvAAAFH3EQhXERh3ESUnETWA4AAABzZXRfYnJlYWtwb2ludHEUiVgHAAAA
c3BlZWR1cHEVRz/wAAAAAAAAWAkAAABzdGFydF9wb3NxFkcAAAAAAAAAAFgQAAAAdGltZXN0YW1w
X2ppdHRlcnEXRwAAAAAAAAAAWAYAAAB0aW1pbmdxGFgJAAAAd2FsbGNsb2NrcRlYDwAAAHVwZGF0
ZV9pbnRlcnZhbHEaRz+keuFHrhR7dS4=
</properties>
		<properties format="pickle" node_id="15">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgGAAAAZGVzaWducQNYBgAAAGJ1dHRlcnEEWAsA
AABmcmVxdWVuY2llc3EFXXEGKEsMS0ZlWAsAAABpZ25vcmVfbmFuc3EHiVgIAAAAbWV0YWRhdGFx
CH1xCVgEAAAAbW9kZXEKWAgAAABiYW5kcGFzc3ELWBAAAABvZmZsaW5lX2ZpbHRmaWx0cQyIWAUA
AABvcmRlcnENSwRYCQAAAHBhc3NfbG9zc3EOR0AIAAAAAAAAWBMAAABzYXZlZFdpZGdldEdlb21l
dHJ5cQ9jc2lwCl91bnBpY2tsZV90eXBlCnEQWAwAAABQeVF0NS5RdENvcmVxEVgKAAAAUUJ5dGVB
cnJheXESQ0IB2dDLAAMAAAAAB6gAAALvAAAJNQAABL0AAAepAAADHAAACTQAAAS8AAAAAAAAAAAP
AAAAB6kAAAMcAAAJNAAABLxxE4VxFIdxFVJxFlgOAAAAc2V0X2JyZWFrcG9pbnRxF4lYCgAAAHN0
b3BfYXR0ZW5xGEdASQAAAAAAAHUu
</properties>
		<properties format="pickle" node_id="16">gAN9cQAoWAgAAABtZXRhZGF0YXEBfXECWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQNjc2lwCl91
bnBpY2tsZV90eXBlCnEEWAwAAABQeVF0NS5RdENvcmVxBVgKAAAAUUJ5dGVBcnJheXEGQ0IB2dDL
AAMAAAAABsIAAAOYAAALowAABHkAAAbDAAADxQAAC6IAAAR4AAAAAAAAAAAPAAAABsMAAAPFAAAL
ogAABHhxB4VxCIdxCVJxClgOAAAAc2V0X2JyZWFrcG9pbnRxC4lYBQAAAHZhbHVlcQxYYAAAAEM6
L1VzZXJzL3ZpemxhYl9zdHVkL2lkYXR0MjkwMF9ncjkyL25ldXJvcHlwZS1waXBlbGluZS9CQ0lT
cGVsbGVyVjhfb2ZmbGluZS9CQ0lTcGVsbGVyX0FfNV90aW1lc3ENdS4=
</properties>
		<properties format="pickle" node_id="17">gAN9cQAoWBMAAABiZWdpbm5pbmdfZnJvbV96ZXJvcQGJWBUAAABjb21wZW5zYXRlX2ZpbHRlcl9s
YWdxAolYDwAAAGluY2x1ZGVfbWFya2Vyc3EDiVgNAAAAbWFya2VyX2ZpZWxkc3EEWA0AAAAodXNl
IGRlZmF1bHQpcQVYCAAAAG1ldGFkYXRhcQZ9cQdYBgAAAG9mZnNldHEIRz+mBBiTdLxqWBsAAABv
ZmZzZXRfdHJpZ2dlcnNfc3RhdGVfcmVzZXRxCYhYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxCmNz
aXAKX3VucGlja2xlX3R5cGUKcQtYDAAAAFB5UXQ1LlF0Q29yZXEMWAoAAABRQnl0ZUFycmF5cQ1D
QgHZ0MsAAwAAAAAGwgAAAzUAAAgrAAAE3QAABsMAAANiAAAIKgAABNwAAAAAAAAAAA8AAAAGwwAA
A2IAAAgqAAAE3HEOhXEPh3EQUnERWA4AAABzZXRfYnJlYWtwb2ludHESiVgPAAAAdGltZXN0YW1w
X3BhaXJzcRNoBVgNAAAAdXNlX3RpbWVfYXhpc3EUiXUu
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
            "node6",
            "data",
            "node1",
            "data"
        ],
        [
            "node17",
            "data",
            "node1",
            "output_root"
        ],
        [
            "node17",
            "data",
            "node7",
            "output_root"
        ],
        [
            "node13",
            "data",
            "node2",
            "data"
        ],
        [
            "node2",
            "data",
            "node12",
            "data2"
        ],
        [
            "node11",
            "data",
            "node3",
            "data"
        ],
        [
            "node12",
            "outdata",
            "node4",
            "data"
        ],
        [
            "node4",
            "data",
            "node7",
            "data"
        ],
        [
            "node8",
            "data",
            "node5",
            "data"
        ],
        [
            "node5",
            "data",
            "node9",
            "data1"
        ],
        [
            "node5",
            "data",
            "node14",
            "data"
        ],
        [
            "node5",
            "data",
            "node12",
            "data1"
        ],
        [
            "node9",
            "outdata",
            "node6",
            "data"
        ],
        [
            "node10",
            "data",
            "node8",
            "data"
        ],
        [
            "node15",
            "data",
            "node9",
            "data2"
        ],
        [
            "node16",
            "data",
            "node15",
            "data"
        ],
        [
            "node3",
            "data",
            "node18",
            "data"
        ],
        [
            "node18",
            "data",
            "node13",
            "data"
        ],
        [
            "node18",
            "data",
            "node16",
            "data"
        ]
    ],
    "nodes": {
        "node1": {
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
                    "value": "zerophase-dejittered-shifted43mspositive-iir-4order-12to70-eeg-and-dejittered-unity-frequencies-Yformat.xdf"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "output_root": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "C:/Users/vizlab_stud/idatt2900_gr92/neuropype-pipeline/BCISpellerV8_offline/BCISpeller_A_5_times"
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
            "uuid": "1b1c8b70-60c3-42b3-80ff-7baf2c9f7529"
        },
        "node10": {
            "class": "ImportXDF",
            "module": "neuropype.nodes.file_system.ImportXDF",
            "params": {
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
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "C:/Users/vizlab_stud/idatt2900_gr92/neuropype-pipeline/BCISpellerV8/BCISpeller_A_5_times/dejittered-unity-frequencies-Yformat.xdf"
                },
                "handle_clock_resets": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "handle_clock_sync": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "handle_jitter_removal": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "max_marker_len": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "reorder_timestamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "retain_streams": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "use_caching": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "use_streamnames": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "29ee8052-0944-4af5-9c0b-4fd9c7d11fa1"
        },
        "node11": {
            "class": "ImportXDF",
            "module": "neuropype.nodes.file_system.ImportXDF",
            "params": {
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
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "C:/Users/vizlab_stud/idatt2900_gr92/neuropype-pipeline/BCISpellerV8/BCISpeller_A_5_times/dejittered-eeg.xdf"
                },
                "handle_clock_resets": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "handle_clock_sync": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "handle_jitter_removal": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "max_marker_len": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "reorder_timestamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "retain_streams": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "use_caching": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "use_streamnames": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "e16fe69e-fc54-47fa-adb4-f51a2e7862a1"
        },
        "node12": {
            "class": "MergeStreams",
            "module": "neuropype.nodes.formatting.MergeStreams",
            "params": {
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "replace_if_exists": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "sorting": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "input"
                }
            },
            "uuid": "8d343c29-6b6e-4e0d-b9b4-8a71ca5d8335"
        },
        "node13": {
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
                        12,
                        27
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
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "order": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 4
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
            "uuid": "d5ca0e90-d3fd-40e7-adec-db0b722e2529"
        },
        "node14": {
            "class": "TimeSeriesPlot",
            "module": "neuropype.nodes.visualization.TimeSeriesPlot",
            "params": {
                "absolute_time": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
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
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "autoscale": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
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
                    "customized": true,
                    "type": "IntPort",
                    "value": 1
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "nans_as_zero": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
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
                    "customized": false,
                    "type": "FloatPort",
                    "value": 1.0
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
                    "customized": false,
                    "type": "FloatPort",
                    "value": 5.0
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
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                }
            },
            "uuid": "702cbd9e-9163-4c9c-ba14-3a82f57535f2"
        },
        "node15": {
            "class": "StreamData",
            "module": "neuropype.nodes.formatting.StreamData",
            "params": {
                "data_dtype": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "float64"
                },
                "data_range_to_stream": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "legacy-warn"
                },
                "hitch_probability": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0
                },
                "jitter_percent": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 5
                },
                "log_progress": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "looping": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "randseed": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 34535
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "speedup": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 1.0
                },
                "start_pos": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0
                },
                "timestamp_jitter": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0
                },
                "timing": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "wallclock"
                },
                "update_interval": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.04
                }
            },
            "uuid": "9a679611-4af4-4fb0-877e-425e3be205f2"
        },
        "node16": {
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
                        12,
                        70
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
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "order": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 4
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
            "uuid": "3140d8e9-d35b-41e6-a0d5-8e50e9335571"
        },
        "node17": {
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
                    "value": "C:/Users/vizlab_stud/idatt2900_gr92/neuropype-pipeline/BCISpellerV8_offline/BCISpeller_A_5_times"
                }
            },
            "uuid": "70d04b47-8c05-417b-8b37-15c584fe3679"
        },
        "node18": {
            "class": "ShiftTimestamps",
            "module": "neuropype.nodes.utilities.ShiftTimestamps",
            "params": {
                "beginning_from_zero": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "compensate_filter_lag": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "include_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_fields": {
                    "customized": false,
                    "type": "ListPort",
                    "value": null
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "offset": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 0.043
                },
                "offset_triggers_state_reset": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "timestamp_pairs": {
                    "customized": false,
                    "type": "ListPort",
                    "value": null
                },
                "use_time_axis": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "02074e53-f041-4a35-ba59-e5ace492f09c"
        },
        "node2": {
            "class": "StreamData",
            "module": "neuropype.nodes.formatting.StreamData",
            "params": {
                "data_dtype": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "float64"
                },
                "data_range_to_stream": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "legacy-warn"
                },
                "hitch_probability": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0
                },
                "jitter_percent": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 5
                },
                "log_progress": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "looping": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "randseed": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 34535
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "speedup": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 1.0
                },
                "start_pos": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0
                },
                "timestamp_jitter": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0
                },
                "timing": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "wallclock"
                },
                "update_interval": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.04
                }
            },
            "uuid": "fa111a4d-63ac-4e2a-850f-9133849d8491"
        },
        "node3": {
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
            "uuid": "82647279-931a-49fa-88ff-9218d8b90db3"
        },
        "node4": {
            "class": "FuseStreams",
            "module": "neuropype.nodes.formatting.FuseStreams",
            "params": {
                "buffer_delay": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 2
                },
                "desired_headroom": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 5
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "min_headroom": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 2
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "srate": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 250
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "eeg"
                },
                "verbosity": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1
                }
            },
            "uuid": "5614d095-09c2-45ba-b244-d789837e7359"
        },
        "node5": {
            "class": "StreamData",
            "module": "neuropype.nodes.formatting.StreamData",
            "params": {
                "data_dtype": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "float64"
                },
                "data_range_to_stream": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "legacy-warn"
                },
                "hitch_probability": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0
                },
                "jitter_percent": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 5
                },
                "log_progress": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "looping": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "randseed": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 34535
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "speedup": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 1.0
                },
                "start_pos": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0
                },
                "timestamp_jitter": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0
                },
                "timing": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "wallclock"
                },
                "update_interval": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.04
                }
            },
            "uuid": "98b2ba1c-99f7-49a2-a8c8-e224ad82e6b2"
        },
        "node6": {
            "class": "FuseStreams",
            "module": "neuropype.nodes.formatting.FuseStreams",
            "params": {
                "buffer_delay": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 2
                },
                "desired_headroom": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 5
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "min_headroom": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 2
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "srate": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 250
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "eeg"
                },
                "verbosity": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1
                }
            },
            "uuid": "55d3288d-4f98-4c89-ad1a-e529f5a1d366"
        },
        "node7": {
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
                    "value": "zerophase-dejittered-shifted43mspositive-iir-4order-12to27-eeg-and-dejittered-unity-frequencies-Yformat.xdf"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "output_root": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "C:/Users/vizlab_stud/idatt2900_gr92/neuropype-pipeline/BCISpellerV8_offline/BCISpeller_A_5_times"
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
            "uuid": "f4f62075-6f01-4645-9657-afcc7bac336b"
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
            "uuid": "a87cd633-27d1-40b7-abfc-1de148e49914"
        },
        "node9": {
            "class": "MergeStreams",
            "module": "neuropype.nodes.formatting.MergeStreams",
            "params": {
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "replace_if_exists": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "sorting": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "input"
                }
            },
            "uuid": "32d56b91-a58f-451d-9299-2461b90d5c4b"
        }
    },
    "version": 1.1
}</patch>
</scheme>
