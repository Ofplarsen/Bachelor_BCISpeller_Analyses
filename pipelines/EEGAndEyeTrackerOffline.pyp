<?xml version='1.0' encoding='utf-8'?>
<scheme description="" title="EEGAndEyeTrackerOffline" version="2.0">
	<nodes>
		<node id="0" name="Import XDF" position="(541.0, 752.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportxdf.OWImportXDF" title="Import XDF" uuid="eca9558e-8a69-455d-a4ee-2d1cd3d74123" version="1.4.2" />
		<node id="1" name="IIR Filter" position="(764.0, 766.0)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owiirfilter.OWIIRFilter" title="IIR Filter (3)" uuid="f340a094-b16b-46e4-9b80-1281d6d5d6b7" version="1.1.0" />
		<node id="2" name="Dejitter Timestamps" position="(606.0, 762.0)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps (3)" uuid="4b799bb2-4f74-440d-9fdd-4986bfe81dd5" version="1.0.0" />
		<node id="3" name="Record to XDF" position="(1146.0, 762.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF (1)" uuid="d367b5db-1420-4866-a074-07806b391bda" version="1.4.0" />
		<node id="4" name="Constant String" position="(288.0, 429.0)" project_name="NeuroPype" qualified_name="widgets.programming.owconstantstring.OWConstantString" title="Base root" uuid="0af81b12-be93-436e-99a4-a16ed6ee9666" version="1.0.0" />
		<node id="5" name="Constant String" position="(289.0, 234.0)" project_name="NeuroPype" qualified_name="widgets.programming.owconstantstring.OWConstantString" title="Input data dir" uuid="703bfd45-23b2-4162-a955-d3c05b660555" version="1.0.0" />
		<node id="6" name="Constant String" position="(285.0, 120.0)" project_name="NeuroPype" qualified_name="widgets.programming.owconstantstring.OWConstantString" title="Input data dir index" uuid="d2955b43-2f6a-4c6c-a28e-89f47f33b4df" version="1.0.0" />
		<node id="7" name="String Concatenate" position="(495.0, 328.0)" project_name="NeuroPype" qualified_name="widgets.programming.owstringconcat.OWStringConcat" title="Concatenated Base Dir" uuid="87fd9e58-574a-4d5d-8678-aef3986580d2" version="1.0.0" />
		<node id="8" name="Constant String" position="(680.0, 345.0)" project_name="NeuroPype" qualified_name="widgets.programming.owconstantstring.OWConstantString" title="Offline" uuid="1c4835a7-0147-4ccc-bd17-a3336a9c429c" version="1.0.0" />
		<node id="9" name="String Concatenate" position="(1029.0, 194.0)" project_name="NeuroPype" qualified_name="widgets.programming.owstringconcat.OWStringConcat" title="Concatenated Output File Name p1" uuid="2451283f-03f5-44fb-80f5-c3c128ce5b16" version="1.0.0" />
		<node id="10" name="Constant String" position="(683.0, 469.0)" project_name="NeuroPype" qualified_name="widgets.programming.owconstantstring.OWConstantString" title="Forward slash" uuid="0c297e68-1bf7-414f-9d44-eac41d066659" version="1.0.0" />
		<node id="11" name="String Concatenate" position="(143.0, 744.0)" project_name="NeuroPype" qualified_name="widgets.programming.owstringconcat.OWStringConcat" title="Concatenated Input Dir Name" uuid="3af1d4d9-6c00-46ec-943d-578c65e69064" version="1.0.0" />
		<node id="12" name="Constant String" position="(371.0, 815.0)" project_name="NeuroPype" qualified_name="widgets.programming.owconstantstring.OWConstantString" title="Raw EEG" uuid="e1b84911-645f-4578-ac4e-cfe968be6099" version="1.0.0" />
		<node id="13" name="String Concatenate" position="(461.0, 739.0)" project_name="NeuroPype" qualified_name="widgets.programming.owstringconcat.OWStringConcat" title="Concatenated EEG Input File Name" uuid="90fa5dd6-a58c-48c4-a4fc-1fc8d64bd10e" version="1.0.0" />
		<node id="14" name="String Concatenate" position="(1214.0, 188.0)" project_name="NeuroPype" qualified_name="widgets.programming.owstringconcat.OWStringConcat" title="Concatenated Output File Name p2" uuid="25338d82-f66d-4468-8ead-618ab862dbb1" version="1.0.0" />
		<node id="15" name="Import XDF" position="(568.0, 1110.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportxdf.OWImportXDF" title="Import XDF (1)" uuid="69b54bfb-6435-4b0e-a3dd-1773b79259a6" version="1.4.2" />
		<node id="16" name="Dejitter Timestamps" position="(692.0, 1108.0)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps" uuid="de330b05-ecff-4cb3-aff7-30313970a9ef" version="1.0.0" />
		<node id="17" name="Record to XDF" position="(1105.0, 1100.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF" uuid="9c15c18c-8972-476b-9163-bbdc7742add2" version="1.4.0" />
		<node id="18" name="String Concatenate" position="(444.0, 958.0)" project_name="NeuroPype" qualified_name="widgets.programming.owstringconcat.OWStringConcat" title="Concatenated GaB Input File Name" uuid="6487313d-380e-4e1a-a717-b81a999d60f3" version="1.0.0" />
		<node id="19" name="Constant String" position="(336.0, 1041.0)" project_name="NeuroPype" qualified_name="widgets.programming.owconstantstring.OWConstantString" title="Gaze and blinking" uuid="b30b2d35-ffe1-4a8d-b43b-cf864b100192" version="1.0.0" />
		<node id="20" name="Decimate" position="(676.0, 765.0)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owdecimate.OWDecimate" title="Decimate" uuid="e0889df6-301b-4f83-a088-f293aa9efbd8" version="1.0.1" />
		<node id="21" name="Stream Data" position="(783.0, 1107.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owstreamdata.OWStreamData" title="Stream Data" uuid="a68ca0eb-069c-4942-9738-c55ffe1c7c7c" version="1.3.0" />
		<node id="22" name="Merge Streams" position="(938.0, 766.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owmergestreams.OWMergeStreams" title="Merge Streams" uuid="2c81289a-a22d-40c9-9793-e8f827ac8ad6" version="1.0.0" />
		<node id="23" name="Fuse Streams" position="(1020.0, 774.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owfusestreams.OWFuseStreams" title="Fuse Streams" uuid="feae7103-c215-40f0-ab90-55c876e80a97" version="0.9.6" />
		<node id="24" name="Fuse Streams" position="(992.0, 1110.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owfusestreams.OWFuseStreams" title="Fuse Streams (1)" uuid="8e7ea45d-6756-4ea4-8dc8-103bddfdbc5f" version="0.9.6" />
		<node id="25" name="Stream Data" position="(857.0, 773.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owstreamdata.OWStreamData" title="Stream Data (1)" uuid="346e4363-bea1-46ac-8009-aefd3fbfd5d3" version="1.3.0" />
		<node id="26" name="Merge Streams" position="(887.0, 1112.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owmergestreams.OWMergeStreams" title="Merge Streams (1)" uuid="540cb134-435a-4f71-90ce-a3469145859e" version="1.0.0" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="2" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="1" sink_channel="Data1" sink_node_id="7" source_channel="Data" source_node_id="4" />
		<link enabled="true" id="2" sink_channel="Data2" sink_node_id="7" source_channel="Data" source_node_id="5" />
		<link enabled="true" id="3" sink_channel="Data1" sink_node_id="9" source_channel="Outstring" source_node_id="7" />
		<link enabled="true" id="4" sink_channel="Data2" sink_node_id="9" source_channel="Data" source_node_id="8" />
		<link enabled="true" id="5" sink_channel="Data3" sink_node_id="9" source_channel="Data" source_node_id="10" />
		<link enabled="true" id="6" sink_channel="Data4" sink_node_id="9" source_channel="Data" source_node_id="5" />
		<link enabled="true" id="7" sink_channel="Data1" sink_node_id="11" source_channel="Outstring" source_node_id="7" />
		<link enabled="true" id="8" sink_channel="Data2" sink_node_id="11" source_channel="Data" source_node_id="10" />
		<link enabled="true" id="9" sink_channel="Data3" sink_node_id="11" source_channel="Data" source_node_id="5" />
		<link enabled="true" id="10" sink_channel="Data4" sink_node_id="11" source_channel="Data" source_node_id="6" />
		<link enabled="true" id="11" sink_channel="Data1" sink_node_id="13" source_channel="Outstring" source_node_id="11" />
		<link enabled="true" id="12" sink_channel="Data2" sink_node_id="13" source_channel="Data" source_node_id="12" />
		<link enabled="true" id="13" sink_channel="Filename" sink_node_id="0" source_channel="Outstring" source_node_id="13" />
		<link enabled="true" id="14" sink_channel="Data1" sink_node_id="14" source_channel="Outstring" source_node_id="9" />
		<link enabled="true" id="15" sink_channel="Data2" sink_node_id="14" source_channel="Data" source_node_id="6" />
		<link enabled="true" id="16" sink_channel="Output Root" sink_node_id="3" source_channel="Outstring" source_node_id="14" />
		<link enabled="true" id="17" sink_channel="Data" sink_node_id="16" source_channel="Data" source_node_id="15" />
		<link enabled="true" id="18" sink_channel="Data1" sink_node_id="18" source_channel="Outstring" source_node_id="11" />
		<link enabled="true" id="19" sink_channel="Data2" sink_node_id="18" source_channel="Data" source_node_id="19" />
		<link enabled="true" id="20" sink_channel="Filename" sink_node_id="15" source_channel="Outstring" source_node_id="18" />
		<link enabled="true" id="21" sink_channel="Output Root" sink_node_id="17" source_channel="Outstring" source_node_id="14" />
		<link enabled="true" id="22" sink_channel="Data" sink_node_id="1" source_channel="Data" source_node_id="20" />
		<link enabled="true" id="23" sink_channel="Data" sink_node_id="21" source_channel="Data" source_node_id="16" />
		<link enabled="true" id="24" sink_channel="Data" sink_node_id="23" source_channel="Outdata" source_node_id="22" />
		<link enabled="true" id="25" sink_channel="Data" sink_node_id="3" source_channel="Data" source_node_id="23" />
		<link enabled="true" id="26" sink_channel="Data" sink_node_id="17" source_channel="Data" source_node_id="24" />
		<link enabled="true" id="27" sink_channel="Data" sink_node_id="25" source_channel="Data" source_node_id="1" />
		<link enabled="true" id="28" sink_channel="Data1" sink_node_id="22" source_channel="Data" source_node_id="25" />
		<link enabled="true" id="29" sink_channel="Data1" sink_node_id="26" source_channel="Data" source_node_id="21" />
		<link enabled="true" id="30" sink_channel="Data" sink_node_id="24" source_channel="Outdata" source_node_id="26" />
		<link enabled="true" id="31" sink_channel="Data" sink_node_id="20" source_channel="Data" source_node_id="2" />
	</links>
	<annotations>
		<text font-family="Helvetica" font-size="16" id="0" rect="(1209.0, 727.0, 345.0, 69.0)">Recording dejittered + decimated + [0.75,5] + 4th order + offline filtfilt, aka zerophase, IIR</text>
		<text font-family="Helvetica" font-size="16" id="1" rect="(41.0, 104.0, 216.0, 50.0)">This one needs to change</text>
		<text font-family="Helvetica" font-size="16" id="2" rect="(38.0, 216.0, 206.0, 50.0)">This one needs to change</text>
		<text font-family="Helvetica" font-size="16" id="3" rect="(531.0, 1216.0, 441.0, 96.0)">A very special purpose pipeline for zerophasing EEG data. String concatenations based on the group's filepaths, and is most likely not applicable for other users. Note also that at the time of writing this pipeline, a bug in NP makes concat string node ignore Data5 input.</text>
		<arrow end="(507.0, 1260.0)" fill="#C1272D" id="4" start="(253.0, 1255.0)" />
		<arrow end="(997.0, 1259.0)" fill="#C1272D" id="5" start="(1349.0, 1255.0)" />
	</annotations>
	<thumbnail />
	<node_properties>
		<properties format="pickle" node_id="0">gAN9cQAoWA0AAABjbG91ZF9hY2NvdW50cQFYAAAAAHECWAwAAABjbG91ZF9idWNrZXRxA2gCWBEA
AABjbG91ZF9jcmVkZW50aWFsc3EEaAJYCgAAAGNsb3VkX2hvc3RxBVgHAAAARGVmYXVsdHEGWAgA
AABmaWxlbmFtZXEHaAJYEwAAAGhhbmRsZV9jbG9ja19yZXNldHNxCIhYEQAAAGhhbmRsZV9jbG9j
a19zeW5jcQmIWBUAAABoYW5kbGVfaml0dGVyX3JlbW92YWxxCohYDgAAAG1heF9tYXJrZXJfbGVu
cQtYDQAAACh1c2UgZGVmYXVsdClxDFgIAAAAbWV0YWRhdGFxDX1xDlgSAAAAcmVvcmRlcl90aW1l
c3RhbXBzcQ+JWA4AAAByZXRhaW5fc3RyZWFtc3EQWA0AAAAodXNlIGRlZmF1bHQpcRFYEwAAAHNh
dmVkV2lkZ2V0R2VvbWV0cnlxEmNzaXAKX3VucGlja2xlX3R5cGUKcRNYDAAAAFB5UXQ1LlF0Q29y
ZXEUWAoAAABRQnl0ZUFycmF5cRVDQgHZ0MsAAwAAAAAC0AAAA9AAAAcTAAAGKwAAAtEAAAP9AAAH
EgAABioAAAAAAAAAAA8AAAAC0QAAA/0AAAcSAAAGKnEWhXEXh3EYUnEZWA4AAABzZXRfYnJlYWtw
b2ludHEaiVgLAAAAdXNlX2NhY2hpbmdxG4lYDwAAAHVzZV9zdHJlYW1uYW1lc3EciFgHAAAAdmVy
Ym9zZXEdiXUu
</properties>
		<properties format="pickle" node_id="1">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgGAAAAZGVzaWducQNYBgAAAGJ1dHRlcnEEWAsA
AABmcmVxdWVuY2llc3EFXXEGKEc/6AAAAAAAAEsFZVgLAAAAaWdub3JlX25hbnNxB4lYCAAAAG1l
dGFkYXRhcQh9cQlYBAAAAG1vZGVxClgIAAAAYmFuZHBhc3NxC1gQAAAAb2ZmbGluZV9maWx0Zmls
dHEMiFgFAAAAb3JkZXJxDUsEWAkAAABwYXNzX2xvc3NxDkdACAAAAAAAAFgTAAAAc2F2ZWRXaWRn
ZXRHZW9tZXRyeXEPY3NpcApfdW5waWNrbGVfdHlwZQpxEFgMAAAAUHlRdDUuUXRDb3JlcRFYCgAA
AFFCeXRlQXJyYXlxEkNCAdnQywADAAAAAAUwAAADKwAABr0AAAT5AAAFMQAAA1gAAAa8AAAE+AAA
AAAAAAAADwAAAAUxAAADWAAABrwAAAT4cROFcRSHcRVScRZYDgAAAHNldF9icmVha3BvaW50cReJ
WAoAAABzdG9wX2F0dGVucRhHQEkAAAAAAAB1Lg==
</properties>
		<properties format="pickle" node_id="2">gAN9cQAoWA8AAABmb3JjZV9tb25vdG9uaWNxAYhYDwAAAGZvcmdldF9oYWxmdGltZXECS1pYDgAA
AG1heF91cGRhdGVyYXRlcQNN9AFYCAAAAG1ldGFkYXRhcQR9cQVYEwAAAHNhdmVkV2lkZ2V0R2Vv
bWV0cnlxBmNzaXAKX3VucGlja2xlX3R5cGUKcQdYDAAAAFB5UXQ1LlF0Q29yZXEIWAoAAABRQnl0
ZUFycmF5cQlDQgHZ0MsAAwAAAAAGqgAAA2sAAAhEAAAEpwAABqsAAAOYAAAIQwAABKYAAAAAAAAA
AA8AAAAGqwAAA5gAAAhDAAAEpnEKhXELh3EMUnENWA4AAABzZXRfYnJlYWtwb2ludHEOiVgOAAAA
d2FybXVwX3NhbXBsZXNxD0r/////dS4=
</properties>
		<properties format="pickle" node_id="3">gAN9cQAoWAwAAABhbGxvd19kb3VibGVxAYlYDwAAAGNsb3NlX29uX21hcmtlcnECWA8AAABjbG9z
ZS1yZWNvcmRpbmdxA1gNAAAAY2xvdWRfYWNjb3VudHEEWAAAAABxBVgMAAAAY2xvdWRfYnVja2V0
cQZoBVgRAAAAY2xvdWRfY3JlZGVudGlhbHNxB2gFWAoAAABjbG91ZF9ob3N0cQhYBwAAAERlZmF1
bHRxCVgOAAAAY2xvdWRfcGFydHNpemVxCkseWAwAAABkZWxldGVfcGFydHNxC4hYCAAAAGZpbGVu
YW1lcQxYOQAAAHplcm9waGFzZS1kZWppdHRlcmVkLWRlY2ltYXRlZC1paXItNG9yZGVyLTAuNzV0
bzUtZWVnLnhkZnENWAgAAABtZXRhZGF0YXEOfXEPWAsAAABvdXRwdXRfcm9vdHEQaAVYGgAAAHBy
ZXNlcnZlX29yaWdpbmFsX21ldGFkYXRhcRGJWAsAAAByZXRyaWV2YWJsZXESiVgTAAAAc2F2ZWRX
aWRnZXRHZW9tZXRyeXETY3NpcApfdW5waWNrbGVfdHlwZQpxFFgMAAAAUHlRdDUuUXRDb3JlcRVY
CgAAAFFCeXRlQXJyYXlxFkNCAdnQywADAAAAAAOpAAACnwAABzwAAATWAAADqQAAAp8AAAc8AAAE
1gAAAAAAAAAADwAAAAOpAAACnwAABzwAAATWcReFcRiHcRlScRpYDQAAAHNlc3Npb25fbm90ZXNx
G2gFWA4AAABzZXRfYnJlYWtwb2ludHEciVgHAAAAdmVyYm9zZXEdiXUu
</properties>
		<properties format="pickle" node_id="4">gAN9cQAoWAgAAABtZXRhZGF0YXEBfXECWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQNjc2lwCl91
bnBpY2tsZV90eXBlCnEEWAwAAABQeVF0NS5RdENvcmVxBVgKAAAAUUJ5dGVBcnJheXEGQ0IB2dDL
AAMAAAAABsIAAAOYAAAJQAAABHkAAAbDAAADxQAACT8AAAR4AAAAAAAAAAAPAAAABsMAAAPFAAAJ
PwAABHhxB4VxCIdxCVJxClgOAAAAc2V0X2JyZWFrcG9pbnRxC4lYBQAAAHZhbHVlcQxYNwAAAEM6
L1VzZXJzL3ZpemxhYl9zdHVkL2lkYXR0MjkwMF9ncjkyL25ldXJvcHlwZS1waXBlbGluZS9xDXUu
</properties>
		<properties format="pickle" node_id="5">gAN9cQAoWAgAAABtZXRhZGF0YXEBfXECWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQNjc2lwCl91
bnBpY2tsZV90eXBlCnEEWAwAAABQeVF0NS5RdENvcmVxBVgKAAAAUUJ5dGVBcnJheXEGQ0IB2dDL
AAMAAAAABhoAAAM5AAAHgwAABBoAAAYbAAADZgAAB4IAAAQZAAAAAAAAAAAPAAAABhsAAANmAAAH
ggAABBlxB4VxCIdxCVJxClgOAAAAc2V0X2JyZWFrcG9pbnRxC4lYBQAAAHZhbHVlcQxYEAAAAExT
TERhdGEtLTE3LTA0XzJxDXUu
</properties>
		<properties format="pickle" node_id="6">gAN9cQAoWAgAAABtZXRhZGF0YXEBfXECWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQNjc2lwCl91
bnBpY2tsZV90eXBlCnEEWAwAAABQeVF0NS5RdENvcmVxBVgKAAAAUUJ5dGVBcnJheXEGQ0IB2dDL
AAMAAAAABl8AAAM/AAAIFQAABCAAAAZgAAADbAAACBQAAAQfAAAAAAAAAAAPAAAABmAAAANsAAAI
FAAABB9xB4VxCIdxCVJxClgOAAAAc2V0X2JyZWFrcG9pbnRxC4hYBQAAAHZhbHVlcQxYAwAAAC0x
NXENdS4=
</properties>
		<properties format="pickle" node_id="7">gAN9cQAoWAgAAABtZXRhZGF0YXEBfXECWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQNjc2lwCl91
bnBpY2tsZV90eXBlCnEEWAwAAABQeVF0NS5RdENvcmVxBVgKAAAAUUJ5dGVBcnJheXEGQ0IB2dDL
AAMAAAAABsMAAAPVAAAIKgAABGgAAAbDAAAD1QAACCoAAARoAAAAAAAAAAAPAAAABsMAAAPVAAAI
KgAABGhxB4VxCIdxCVJxClgOAAAAc2V0X2JyZWFrcG9pbnRxC4l1Lg==
</properties>
		<properties format="pickle" node_id="8">gAN9cQAoWAgAAABtZXRhZGF0YXEBfXECWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQNjc2lwCl91
bnBpY2tsZV90eXBlCnEEWAwAAABQeVF0NS5RdENvcmVxBVgKAAAAUUJ5dGVBcnJheXEGQ0IB2dDL
AAMAAAAABsIAAAOYAAAIKwAABHkAAAbDAAADxQAACCoAAAR4AAAAAAAAAAAPAAAABsMAAAPFAAAI
KgAABHhxB4VxCIdxCVJxClgOAAAAc2V0X2JyZWFrcG9pbnRxC4lYBQAAAHZhbHVlcQxYCAAAAF9v
ZmZsaW5lcQ11Lg==
</properties>
		<properties format="literal" node_id="9">{'metadata': {}, 'savedWidgetGeometry': None, 'set_breakpoint': False}</properties>
		<properties format="pickle" node_id="10">gAN9cQAoWAgAAABtZXRhZGF0YXEBfXECWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQNjc2lwCl91
bnBpY2tsZV90eXBlCnEEWAwAAABQeVF0NS5RdENvcmVxBVgKAAAAUUJ5dGVBcnJheXEGQ0IB2dDL
AAMAAAAABsIAAAOYAAAIKwAABHkAAAbDAAADxQAACCoAAAR4AAAAAAAAAAAPAAAABsMAAAPFAAAI
KgAABHhxB4VxCIdxCVJxClgOAAAAc2V0X2JyZWFrcG9pbnRxC4lYBQAAAHZhbHVlcQxYAQAAAC9x
DXUu
</properties>
		<properties format="literal" node_id="11">{'metadata': {}, 'savedWidgetGeometry': None, 'set_breakpoint': False}</properties>
		<properties format="pickle" node_id="12">gAN9cQAoWAgAAABtZXRhZGF0YXEBfXECWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQNjc2lwCl91
bnBpY2tsZV90eXBlCnEEWAwAAABQeVF0NS5RdENvcmVxBVgKAAAAUUJ5dGVBcnJheXEGQ0IB2dDL
AAMAAAAAArIAAAZZAAAEGwAABzoAAAKzAAAGhgAABBoAAAc5AAAAAAAAAAAPAAAAArMAAAaGAAAE
GgAABzlxB4VxCIdxCVJxClgOAAAAc2V0X2JyZWFrcG9pbnRxC4lYBQAAAHZhbHVlcQxYDAAAAC9y
YXctZWVnLnhkZnENdS4=
</properties>
		<properties format="literal" node_id="13">{'metadata': {}, 'savedWidgetGeometry': None, 'set_breakpoint': False}</properties>
		<properties format="literal" node_id="14">{'metadata': {}, 'savedWidgetGeometry': None, 'set_breakpoint': False}</properties>
		<properties format="pickle" node_id="15">gAN9cQAoWA0AAABjbG91ZF9hY2NvdW50cQFYAAAAAHECWAwAAABjbG91ZF9idWNrZXRxA2gCWBEA
AABjbG91ZF9jcmVkZW50aWFsc3EEaAJYCgAAAGNsb3VkX2hvc3RxBVgHAAAARGVmYXVsdHEGWAgA
AABmaWxlbmFtZXEHaAJYEwAAAGhhbmRsZV9jbG9ja19yZXNldHNxCIhYEQAAAGhhbmRsZV9jbG9j
a19zeW5jcQmIWBUAAABoYW5kbGVfaml0dGVyX3JlbW92YWxxCohYDgAAAG1heF9tYXJrZXJfbGVu
cQtYDQAAACh1c2UgZGVmYXVsdClxDFgIAAAAbWV0YWRhdGFxDX1xDlgSAAAAcmVvcmRlcl90aW1l
c3RhbXBzcQ+JWA4AAAByZXRhaW5fc3RyZWFtc3EQWA0AAAAodXNlIGRlZmF1bHQpcRFYEwAAAHNh
dmVkV2lkZ2V0R2VvbWV0cnlxEmNzaXAKX3VucGlja2xlX3R5cGUKcRNYDAAAAFB5UXQ1LlF0Q29y
ZXEUWAoAAABRQnl0ZUFycmF5cRVDQgHZ0MsAAwAAAAAGwwAAAwgAAAgqAAAFNQAABsMAAAMIAAAI
KgAABTUAAAAAAAAAAA8AAAAGwwAAAwgAAAgqAAAFNXEWhXEXh3EYUnEZWA4AAABzZXRfYnJlYWtw
b2ludHEaiVgLAAAAdXNlX2NhY2hpbmdxG4lYDwAAAHVzZV9zdHJlYW1uYW1lc3EciFgHAAAAdmVy
Ym9zZXEdiXUu
</properties>
		<properties format="pickle" node_id="16">gAN9cQAoWA8AAABmb3JjZV9tb25vdG9uaWNxAYhYDwAAAGZvcmdldF9oYWxmdGltZXECS1pYDgAA
AG1heF91cGRhdGVyYXRlcQNN9AFYCAAAAG1ldGFkYXRhcQR9cQVYEwAAAHNhdmVkV2lkZ2V0R2Vv
bWV0cnlxBmNzaXAKX3VucGlja2xlX3R5cGUKcQdYDAAAAFB5UXQ1LlF0Q29yZXEIWAoAAABRQnl0
ZUFycmF5cQlDQgHZ0MsAAwAAAAAGqgAAA2sAAAhEAAAEpwAABqsAAAOYAAAIQwAABKYAAAAAAAAA
AA8AAAAGqwAAA5gAAAhDAAAEpnEKhXELh3EMUnENWA4AAABzZXRfYnJlYWtwb2ludHEOiVgOAAAA
d2FybXVwX3NhbXBsZXNxD0r/////dS4=
</properties>
		<properties format="pickle" node_id="17">gAN9cQAoWAwAAABhbGxvd19kb3VibGVxAYlYDwAAAGNsb3NlX29uX21hcmtlcnECWA8AAABjbG9z
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
		<properties format="literal" node_id="18">{'metadata': {}, 'savedWidgetGeometry': None, 'set_breakpoint': False}</properties>
		<properties format="pickle" node_id="19">gAN9cQAoWAgAAABtZXRhZGF0YXEBfXECWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQNjc2lwCl91
bnBpY2tsZV90eXBlCnEEWAwAAABQeVF0NS5RdENvcmVxBVgKAAAAUUJ5dGVBcnJheXEGQ0IB2dDL
AAMAAAAABsIAAAOYAAAIKwAABHkAAAbDAAADxQAACCoAAAR4AAAAAAAAAAAPAAAABsMAAAPFAAAI
KgAABHhxB4VxCIdxCVJxClgOAAAAc2V0X2JyZWFrcG9pbnRxC4lYBQAAAHZhbHVlcQxYFgAAAC9n
YXplLWFuZC1ibGlua2luZy54ZGZxDXUu
</properties>
		<properties format="pickle" node_id="20">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgGAAAAZmFjdG9ycQNLAlgIAAAAbWV0YWRhdGFx
BH1xBVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEGY3NpcApfdW5waWNrbGVfdHlwZQpxB1gMAAAA
UHlRdDUuUXRDb3JlcQhYCgAAAFFCeXRlQXJyYXlxCUNCAdnQywADAAAAAAbCAAADigAACCsAAASI
AAAGwwAAA7cAAAgqAAAEhwAAAAAAAAAADwAAAAbDAAADtwAACCoAAASHcQqFcQuHcQxScQ1YDgAA
AHNldF9icmVha3BvaW50cQ6JdS4=
</properties>
		<properties format="pickle" node_id="21">gAN9cQAoWAoAAABkYXRhX2R0eXBlcQFYBwAAAGZsb2F0NjRxAlgUAAAAZGF0YV9yYW5nZV90b19z
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
		<properties format="literal" node_id="22">{'metadata': {}, 'replace_if_exists': False, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'sorting': 'input'}</properties>
		<properties format="pickle" node_id="23">gAN9cQAoWAwAAABidWZmZXJfZGVsYXlxAUsCWBAAAABkZXNpcmVkX2hlYWRyb29tcQJLBVgIAAAA
bWV0YWRhdGFxA31xBFgMAAAAbWluX2hlYWRyb29tcQVLAlgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRy
eXEGY3NpcApfdW5waWNrbGVfdHlwZQpxB1gMAAAAUHlRdDUuUXRDb3JlcQhYCgAAAFFCeXRlQXJy
YXlxCUNCAdnQywADAAAAAAavAAADSAAACD4AAATJAAAGsAAAA3UAAAg9AAAEyAAAAAAAAAAADwAA
AAawAAADdQAACD0AAATIcQqFcQuHcQxScQ1YDgAAAHNldF9icmVha3BvaW50cQ6JWAUAAABzcmF0
ZXEPS/pYCwAAAHN0cmVhbV9uYW1lcRBYAwAAAGVlZ3ERWAkAAAB2ZXJib3NpdHlxEksBdS4=
</properties>
		<properties format="pickle" node_id="24">gAN9cQAoWAwAAABidWZmZXJfZGVsYXlxAUsCWBAAAABkZXNpcmVkX2hlYWRyb29tcQJLBVgIAAAA
bWV0YWRhdGFxA31xBFgMAAAAbWluX2hlYWRyb29tcQVLAlgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRy
eXEGY3NpcApfdW5waWNrbGVfdHlwZQpxB1gMAAAAUHlRdDUuUXRDb3JlcQhYCgAAAFFCeXRlQXJy
YXlxCUNCAdnQywADAAAAAAavAAADSAAACD4AAATJAAAGsAAAA3UAAAg9AAAEyAAAAAAAAAAADwAA
AAawAAADdQAACD0AAATIcQqFcQuHcQxScQ1YDgAAAHNldF9icmVha3BvaW50cQ6JWAUAAABzcmF0
ZXEPS/pYCwAAAHN0cmVhbV9uYW1lcRBYAwAAAGVlZ3ERWAkAAAB2ZXJib3NpdHlxEksBdS4=
</properties>
		<properties format="pickle" node_id="25">gAN9cQAoWAoAAABkYXRhX2R0eXBlcQFYBwAAAGZsb2F0NjRxAlgUAAAAZGF0YV9yYW5nZV90b19z
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
		<properties format="literal" node_id="26">{'metadata': {}, 'replace_if_exists': False, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'sorting': 'input'}</properties>
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
            "node1",
            "data",
            "node3",
            "data"
        ],
        [
            "node5",
            "data",
            "node8",
            "data1"
        ],
        [
            "node6",
            "data",
            "node8",
            "data2"
        ],
        [
            "node6",
            "data",
            "node10",
            "data4"
        ],
        [
            "node6",
            "data",
            "node12",
            "data3"
        ],
        [
            "node8",
            "outstring",
            "node10",
            "data1"
        ],
        [
            "node8",
            "outstring",
            "node12",
            "data1"
        ],
        [
            "node9",
            "data",
            "node10",
            "data2"
        ],
        [
            "node11",
            "data",
            "node10",
            "data3"
        ],
        [
            "node11",
            "data",
            "node12",
            "data2"
        ],
        [
            "node7",
            "data",
            "node12",
            "data4"
        ],
        [
            "node7",
            "data",
            "node15",
            "data2"
        ],
        [
            "node12",
            "outstring",
            "node14",
            "data1"
        ],
        [
            "node12",
            "outstring",
            "node19",
            "data1"
        ],
        [
            "node13",
            "data",
            "node14",
            "data2"
        ],
        [
            "node14",
            "outstring",
            "node1",
            "filename"
        ],
        [
            "node10",
            "outstring",
            "node15",
            "data1"
        ],
        [
            "node15",
            "outstring",
            "node4",
            "output_root"
        ],
        [
            "node15",
            "outstring",
            "node18",
            "output_root"
        ],
        [
            "node16",
            "data",
            "node17",
            "data"
        ],
        [
            "node20",
            "data",
            "node19",
            "data2"
        ],
        [
            "node19",
            "outstring",
            "node16",
            "filename"
        ],
        [
            "node21",
            "data",
            "node2",
            "data"
        ],
        [
            "node17",
            "data",
            "node22",
            "data"
        ],
        [
            "node23",
            "outdata",
            "node24",
            "data"
        ],
        [
            "node24",
            "data",
            "node4",
            "data"
        ],
        [
            "node25",
            "data",
            "node18",
            "data"
        ],
        [
            "node2",
            "data",
            "node26",
            "data"
        ],
        [
            "node26",
            "data",
            "node23",
            "data1"
        ],
        [
            "node22",
            "data",
            "node27",
            "data1"
        ],
        [
            "node27",
            "outdata",
            "node25",
            "data"
        ],
        [
            "node3",
            "data",
            "node21",
            "data"
        ]
    ],
    "nodes": {
        "node1": {
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
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
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
            "uuid": "eca9558e-8a69-455d-a4ee-2d1cd3d74123"
        },
        "node10": {
            "class": "StringConcat",
            "module": "neuropype.nodes.programming.StringConcat",
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
                }
            },
            "uuid": "2451283f-03f5-44fb-80f5-c3c128ce5b16"
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
                    "value": "/"
                }
            },
            "uuid": "0c297e68-1bf7-414f-9d44-eac41d066659"
        },
        "node12": {
            "class": "StringConcat",
            "module": "neuropype.nodes.programming.StringConcat",
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
                }
            },
            "uuid": "3af1d4d9-6c00-46ec-943d-578c65e69064"
        },
        "node13": {
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
                    "value": "/raw-eeg.xdf"
                }
            },
            "uuid": "e1b84911-645f-4578-ac4e-cfe968be6099"
        },
        "node14": {
            "class": "StringConcat",
            "module": "neuropype.nodes.programming.StringConcat",
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
                }
            },
            "uuid": "90fa5dd6-a58c-48c4-a4fc-1fc8d64bd10e"
        },
        "node15": {
            "class": "StringConcat",
            "module": "neuropype.nodes.programming.StringConcat",
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
                }
            },
            "uuid": "25338d82-f66d-4468-8ead-618ab862dbb1"
        },
        "node16": {
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
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
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
            "uuid": "69b54bfb-6435-4b0e-a3dd-1773b79259a6"
        },
        "node17": {
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
            "uuid": "de330b05-ecff-4cb3-aff7-30313970a9ef"
        },
        "node18": {
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
            "uuid": "9c15c18c-8972-476b-9163-bbdc7742add2"
        },
        "node19": {
            "class": "StringConcat",
            "module": "neuropype.nodes.programming.StringConcat",
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
                }
            },
            "uuid": "6487313d-380e-4e1a-a717-b81a999d60f3"
        },
        "node2": {
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
            "uuid": "f340a094-b16b-46e4-9b80-1281d6d5d6b7"
        },
        "node20": {
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
                    "value": "/gaze-and-blinking.xdf"
                }
            },
            "uuid": "b30b2d35-ffe1-4a8d-b43b-cf864b100192"
        },
        "node21": {
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
            "uuid": "e0889df6-301b-4f83-a088-f293aa9efbd8"
        },
        "node22": {
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
            "uuid": "a68ca0eb-069c-4942-9738-c55ffe1c7c7c"
        },
        "node23": {
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
            "uuid": "2c81289a-a22d-40c9-9793-e8f827ac8ad6"
        },
        "node24": {
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
            "uuid": "feae7103-c215-40f0-ab90-55c876e80a97"
        },
        "node25": {
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
            "uuid": "8e7ea45d-6756-4ea4-8dc8-103bddfdbc5f"
        },
        "node26": {
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
            "uuid": "346e4363-bea1-46ac-8009-aefd3fbfd5d3"
        },
        "node27": {
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
            "uuid": "540cb134-435a-4f71-90ce-a3469145859e"
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
            "uuid": "4b799bb2-4f74-440d-9fdd-4986bfe81dd5"
        },
        "node4": {
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
                    "value": "zerophase-dejittered-decimated-iir-4order-0.75to5-eeg.xdf"
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
            "uuid": "d367b5db-1420-4866-a074-07806b391bda"
        },
        "node5": {
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
                    "value": "C:/Users/vizlab_stud/idatt2900_gr92/neuropype-pipeline/"
                }
            },
            "uuid": "0af81b12-be93-436e-99a4-a16ed6ee9666"
        },
        "node6": {
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
                    "value": "LSLData--17-04_2"
                }
            },
            "uuid": "703bfd45-23b2-4162-a955-d3c05b660555"
        },
        "node7": {
            "class": "ConstantString",
            "module": "neuropype.nodes.programming.ConstantString",
            "params": {
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "set_breakpoint": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "value": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "-15"
                }
            },
            "uuid": "d2955b43-2f6a-4c6c-a28e-89f47f33b4df"
        },
        "node8": {
            "class": "StringConcat",
            "module": "neuropype.nodes.programming.StringConcat",
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
                }
            },
            "uuid": "87fd9e58-574a-4d5d-8678-aef3986580d2"
        },
        "node9": {
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
                    "value": "_offline"
                }
            },
            "uuid": "1c4835a7-0147-4ccc-bd17-a3336a9c429c"
        }
    },
    "version": 1.1
}</patch>
</scheme>
