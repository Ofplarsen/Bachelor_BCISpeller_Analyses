<?xml version='1.0' encoding='utf-8'?>
<scheme description="" title="EEGAndEyeTrackerOffline" version="2.0">
	<nodes>
		<node id="0" name="Import XDF" position="(565.0, 547.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportxdf.OWImportXDF" title="Import XDF" uuid="4882e169-9ea4-49d2-b049-ee5a4678f828" version="1.4.2" />
		<node id="1" name="Fuse Streams" position="(1183.0, 826.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owfusestreams.OWFuseStreams" title="Fuse Streams (1)" uuid="d7059bb8-00c1-4a71-ad32-ab8329263e49" version="0.9.6" />
		<node id="2" name="IIR Filter" position="(839.0, 669.0)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owiirfilter.OWIIRFilter" title="IIR Filter (3)" uuid="e082e490-8250-495e-b757-1dd557641b25" version="1.1.0" />
		<node id="3" name="Merge Streams" position="(1057.0, 808.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owmergestreams.OWMergeStreams" title="Merge Streams (2)" uuid="3c61251e-d45d-4bb9-a2c3-7c3dca4470af" version="1.0.0" />
		<node id="4" name="Record to XDF" position="(1344.0, 840.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF" uuid="d37bc6bb-b9a2-427b-8c57-2e3d8fcdc4de" version="1.4.0" />
		<node id="5" name="Dejitter Timestamps" position="(709.0, 417.0)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps" uuid="5977a75a-1c66-46b0-be7f-e48f95ac0296" version="1.0.0" />
		<node id="6" name="Fuse Streams" position="(1240.0, 456.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owfusestreams.OWFuseStreams" title="Fuse Streams (1)" uuid="a357a75e-bcf6-4cee-83b1-8755518b4c83" version="0.9.6" />
		<node id="7" name="Import XDF" position="(573.0, 434.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportxdf.OWImportXDF" title="Import XDF (2)" uuid="c64eca97-2ec6-4df8-b96a-8511935f6b94" version="1.4.2" />
		<node id="8" name="Stream Data" position="(981.0, 554.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owstreamdata.OWStreamData" title="Stream Data (3)" uuid="8886e51c-e312-49d6-8a2d-60dda623443f" version="1.3.0" />
		<node id="9" name="Time Series Plot" position="(919.0, 305.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" title="Time Series Plot (1)" uuid="882be015-6ce9-4447-a2e4-1e438c5958f8" version="1.1.0" />
		<node id="10" name="Stream Data" position="(980.0, 423.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owstreamdata.OWStreamData" title="Stream Data (4)" uuid="ee3f478d-761b-46c0-914d-704bd7f0e2d2" version="1.3.0" />
		<node id="11" name="Merge Streams" position="(1114.0, 438.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owmergestreams.OWMergeStreams" title="Merge Streams (2)" uuid="7f2c83de-5852-45ec-b928-97a9f563422a" version="1.0.0" />
		<node id="12" name="Dejitter Timestamps" position="(693.0, 557.0)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps (3)" uuid="67fa89e4-2bb0-4a8a-be3c-b084c007f751" version="1.0.0" />
		<node id="13" name="Record to XDF" position="(1400.0, 471.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF" uuid="abcaa821-2495-4f49-90e8-204a16e1c1a2" version="1.4.0" />
		<node id="14" name="Stream Data" position="(953.0, 906.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owstreamdata.OWStreamData" title="Stream Data (3)" uuid="45294263-66c4-475f-9fd9-db7a9d4de313" version="1.3.0" />
		<node id="15" name="Constant String" position="(1536.0, 646.0)" project_name="NeuroPype" qualified_name="widgets.programming.owconstantstring.OWConstantString" title="Constant String" uuid="df880262-dea3-4d52-a815-99a69bde2c1b" version="1.0.0" />
		<node id="16" name="IIR Filter" position="(840.0, 508.0)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owiirfilter.OWIIRFilter" title="IIR Filter (3)" uuid="a1ac81f4-13cc-44e9-9caa-880e6a5fa277" version="1.1.0" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="12" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="1" sink_channel="Data" sink_node_id="1" source_channel="Outdata" source_node_id="3" />
		<link enabled="true" id="2" sink_channel="Data" sink_node_id="4" source_channel="Data" source_node_id="1" />
		<link enabled="true" id="3" sink_channel="Data" sink_node_id="2" source_channel="Data" source_node_id="12" />
		<link enabled="true" id="4" sink_channel="Data" sink_node_id="14" source_channel="Data" source_node_id="2" />
		<link enabled="true" id="5" sink_channel="Data2" sink_node_id="3" source_channel="Data" source_node_id="14" />
		<link enabled="true" id="6" sink_channel="Data1" sink_node_id="3" source_channel="Data" source_node_id="10" />
		<link enabled="true" id="7" sink_channel="Output Root" sink_node_id="4" source_channel="Data" source_node_id="15" />
		<link enabled="true" id="8" sink_channel="Data" sink_node_id="5" source_channel="Data" source_node_id="7" />
		<link enabled="true" id="9" sink_channel="Data" sink_node_id="10" source_channel="Data" source_node_id="5" />
		<link enabled="true" id="10" sink_channel="Data" sink_node_id="6" source_channel="Outdata" source_node_id="11" />
		<link enabled="true" id="11" sink_channel="Data" sink_node_id="13" source_channel="Data" source_node_id="6" />
		<link enabled="true" id="12" sink_channel="Data" sink_node_id="8" source_channel="Data" source_node_id="16" />
		<link enabled="true" id="13" sink_channel="Data2" sink_node_id="11" source_channel="Data" source_node_id="8" />
		<link enabled="true" id="14" sink_channel="Data" sink_node_id="9" source_channel="Data" source_node_id="10" />
		<link enabled="true" id="15" sink_channel="Data1" sink_node_id="11" source_channel="Data" source_node_id="10" />
		<link enabled="true" id="16" sink_channel="Data" sink_node_id="16" source_channel="Data" source_node_id="12" />
		<link enabled="true" id="17" sink_channel="Output Root" sink_node_id="13" source_channel="Data" source_node_id="15" />
	</links>
	<annotations>
		<text font-family="Helvetica" font-size="16" id="0" rect="(1045.0, 287.0, 353.0, 80.0)">Merging dejittered + [1,28] + 4th order + offline filtfilt IIR and dejittered eye tracker</text>
		<text font-family="Helvetica" font-size="16" id="1" rect="(1076.0, 693.0, 345.0, 66.0)">Merging dejittered + [0.75,5] + 4th order + offline filtfilt IIR and dejittered eye tracker</text>
	</annotations>
	<thumbnail />
	<node_properties>
		<properties format="pickle" node_id="0">gAN9cQAoWA0AAABjbG91ZF9hY2NvdW50cQFYAAAAAHECWAwAAABjbG91ZF9idWNrZXRxA2gCWBEA
AABjbG91ZF9jcmVkZW50aWFsc3EEaAJYCgAAAGNsb3VkX2hvc3RxBVgHAAAARGVmYXVsdHEGWAgA
AABmaWxlbmFtZXEHWHEAAABDOi9Vc2Vycy92aXpsYWJfc3R1ZC9pZGF0dDI5MDBfZ3I5Mi9uZXVy
b3B5cGUtcGlwZWxpbmUvTFNMRGF0YV9mYXN0X2JsaW5rc1YyL0xTTERhdGFfZmFzdF9ibGlua3NW
Ml8yMC9yYXctZWVnLnhkZnEIWBMAAABoYW5kbGVfY2xvY2tfcmVzZXRzcQmIWBEAAABoYW5kbGVf
Y2xvY2tfc3luY3EKiFgVAAAAaGFuZGxlX2ppdHRlcl9yZW1vdmFscQuIWA4AAABtYXhfbWFya2Vy
X2xlbnEMWA0AAAAodXNlIGRlZmF1bHQpcQ1YCAAAAG1ldGFkYXRhcQ59cQ9YEgAAAHJlb3JkZXJf
dGltZXN0YW1wc3EQiVgOAAAAcmV0YWluX3N0cmVhbXNxEVgNAAAAKHVzZSBkZWZhdWx0KXESWBMA
AABzYXZlZFdpZGdldEdlb21ldHJ5cRNjc2lwCl91bnBpY2tsZV90eXBlCnEUWAwAAABQeVF0NS5R
dENvcmVxFVgKAAAAUUJ5dGVBcnJheXEWQ0IB2dDLAAMAAAAAAtAAAAPQAAAHEwAABisAAALRAAAD
/QAABxIAAAYqAAAAAAAAAAAPAAAAAtEAAAP9AAAHEgAABipxF4VxGIdxGVJxGlgOAAAAc2V0X2Jy
ZWFrcG9pbnRxG4lYCwAAAHVzZV9jYWNoaW5ncRyJWA8AAAB1c2Vfc3RyZWFtbmFtZXNxHYhYBwAA
AHZlcmJvc2VxHol1Lg==
</properties>
		<properties format="pickle" node_id="1">gAN9cQAoWAwAAABidWZmZXJfZGVsYXlxAUsCWBAAAABkZXNpcmVkX2hlYWRyb29tcQJLBVgIAAAA
bWV0YWRhdGFxA31xBFgMAAAAbWluX2hlYWRyb29tcQVLAlgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRy
eXEGY3NpcApfdW5waWNrbGVfdHlwZQpxB1gMAAAAUHlRdDUuUXRDb3JlcQhYCgAAAFFCeXRlQXJy
YXlxCUNCAdnQywADAAAAAAavAAADSAAACD4AAATJAAAGsAAAA3UAAAg9AAAEyAAAAAAAAAAADwAA
AAawAAADdQAACD0AAATIcQqFcQuHcQxScQ1YDgAAAHNldF9icmVha3BvaW50cQ6JWAUAAABzcmF0
ZXEPS3hYCwAAAHN0cmVhbV9uYW1lcRBYAwAAAGVlZ3ERWAkAAAB2ZXJib3NpdHlxEksBdS4=
</properties>
		<properties format="pickle" node_id="2">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgGAAAAZGVzaWducQNYBgAAAGJ1dHRlcnEEWAsA
AABmcmVxdWVuY2llc3EFXXEGKEc/6AAAAAAAAEsFZVgLAAAAaWdub3JlX25hbnNxB4lYCAAAAG1l
dGFkYXRhcQh9cQlYBAAAAG1vZGVxClgIAAAAYmFuZHBhc3NxC1gQAAAAb2ZmbGluZV9maWx0Zmls
dHEMiFgFAAAAb3JkZXJxDUsEWAkAAABwYXNzX2xvc3NxDkdACAAAAAAAAFgTAAAAc2F2ZWRXaWRn
ZXRHZW9tZXRyeXEPY3NpcApfdW5waWNrbGVfdHlwZQpxEFgMAAAAUHlRdDUuUXRDb3JlcRFYCgAA
AFFCeXRlQXJyYXlxEkNCAdnQywADAAAAAAawAAADIgAACD0AAATwAAAGsQAAA08AAAg8AAAE7wAA
AAAAAAAADwAAAAaxAAADTwAACDwAAATvcROFcRSHcRVScRZYDgAAAHNldF9icmVha3BvaW50cReJ
WAoAAABzdG9wX2F0dGVucRhHQEkAAAAAAAB1Lg==
</properties>
		<properties format="literal" node_id="3">{'metadata': {}, 'replace_if_exists': False, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'sorting': 'input'}</properties>
		<properties format="pickle" node_id="4">gAN9cQAoWAwAAABhbGxvd19kb3VibGVxAYlYDwAAAGNsb3NlX29uX21hcmtlcnECWA8AAABjbG9z
ZS1yZWNvcmRpbmdxA1gNAAAAY2xvdWRfYWNjb3VudHEEWAAAAABxBVgMAAAAY2xvdWRfYnVja2V0
cQZoBVgRAAAAY2xvdWRfY3JlZGVudGlhbHNxB2gFWAoAAABjbG91ZF9ob3N0cQhYBwAAAERlZmF1
bHRxCVgOAAAAY2xvdWRfcGFydHNpemVxCkseWAwAAABkZWxldGVfcGFydHNxC4hYCAAAAGZpbGVu
YW1lcQxYSgAAAHplcm9waGFzZS1kZWppdHRlcmVkLWlpci00b3JkZXItMC43NXRvNS1lZWctYW5k
LWRlaml0dGVyZWQtZXlldHJhY2tpbmcueGRmcQ1YCAAAAG1ldGFkYXRhcQ59cQ9YCwAAAG91dHB1
dF9yb290cRBoBVgaAAAAcHJlc2VydmVfb3JpZ2luYWxfbWV0YWRhdGFxEYlYCwAAAHJldHJpZXZh
YmxlcRKJWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cRNjc2lwCl91bnBpY2tsZV90eXBlCnEUWAwA
AABQeVF0NS5RdENvcmVxFVgKAAAAUUJ5dGVBcnJheXEWQ0IB2dDLAAMAAAAABsIAAALWAAAKggAA
BTsAAAbDAAADAwAACoEAAAU6AAAAAAAAAAAPAAAABsMAAAMDAAAKgQAABTpxF4VxGIdxGVJxGlgN
AAAAc2Vzc2lvbl9ub3Rlc3EbaAVYDgAAAHNldF9icmVha3BvaW50cRyJWAcAAAB2ZXJib3NlcR2J
dS4=
</properties>
		<properties format="literal" node_id="5">{'force_monotonic': True, 'forget_halftime': 90, 'max_updaterate': 500, 'metadata': {}, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'warmup_samples': -1}</properties>
		<properties format="pickle" node_id="6">gAN9cQAoWAwAAABidWZmZXJfZGVsYXlxAUsCWBAAAABkZXNpcmVkX2hlYWRyb29tcQJLBVgIAAAA
bWV0YWRhdGFxA31xBFgMAAAAbWluX2hlYWRyb29tcQVLAlgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRy
eXEGY3NpcApfdW5waWNrbGVfdHlwZQpxB1gMAAAAUHlRdDUuUXRDb3JlcQhYCgAAAFFCeXRlQXJy
YXlxCUNCAdnQywADAAAAAAavAAADSAAACD4AAATJAAAGsAAAA3UAAAg9AAAEyAAAAAAAAAAADwAA
AAawAAADdQAACD0AAATIcQqFcQuHcQxScQ1YDgAAAHNldF9icmVha3BvaW50cQ6JWAUAAABzcmF0
ZXEPS3hYCwAAAHN0cmVhbV9uYW1lcRBYAwAAAGVlZ3ERWAkAAAB2ZXJib3NpdHlxEksBdS4=
</properties>
		<properties format="pickle" node_id="7">gAN9cQAoWA0AAABjbG91ZF9hY2NvdW50cQFYAAAAAHECWAwAAABjbG91ZF9idWNrZXRxA2gCWBEA
AABjbG91ZF9jcmVkZW50aWFsc3EEaAJYCgAAAGNsb3VkX2hvc3RxBVgHAAAARGVmYXVsdHEGWAgA
AABmaWxlbmFtZXEHWHsAAABDOi9Vc2Vycy92aXpsYWJfc3R1ZC9pZGF0dDI5MDBfZ3I5Mi9uZXVy
b3B5cGUtcGlwZWxpbmUvTFNMRGF0YV9mYXN0X2JsaW5rc1YyL0xTTERhdGFfZmFzdF9ibGlua3NW
Ml8yMC9nYXplLWFuZC1ibGlua2luZy54ZGZxCFgTAAAAaGFuZGxlX2Nsb2NrX3Jlc2V0c3EJiFgR
AAAAaGFuZGxlX2Nsb2NrX3N5bmNxCohYFQAAAGhhbmRsZV9qaXR0ZXJfcmVtb3ZhbHELiFgOAAAA
bWF4X21hcmtlcl9sZW5xDFgNAAAAKHVzZSBkZWZhdWx0KXENWAgAAABtZXRhZGF0YXEOfXEPWBIA
AAByZW9yZGVyX3RpbWVzdGFtcHNxEIlYDgAAAHJldGFpbl9zdHJlYW1zcRFYDQAAACh1c2UgZGVm
YXVsdClxElgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXETY3NpcApfdW5waWNrbGVfdHlwZQpxFFgM
AAAAUHlRdDUuUXRDb3JlcRVYCgAAAFFCeXRlQXJyYXlxFkNCAdnQywADAAAAAAKaAAABYwAABxMA
AAO+AAACmwAAAZAAAAcSAAADvQAAAAAAAAAADwAAAAKbAAABkAAABxIAAAO9cReFcRiHcRlScRpY
DgAAAHNldF9icmVha3BvaW50cRuJWAsAAAB1c2VfY2FjaGluZ3EciVgPAAAAdXNlX3N0cmVhbW5h
bWVzcR2IWAcAAAB2ZXJib3NlcR6JdS4=
</properties>
		<properties format="literal" node_id="8">{'data_dtype': 'float64', 'data_range_to_stream': 'legacy-warn', 'hitch_probability': 0.0, 'jitter_percent': 5, 'log_progress': False, 'looping': True, 'metadata': {}, 'randseed': 34535, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'speedup': 1.0, 'start_pos': 0.0, 'timestamp_jitter': 0.0, 'timing': 'wallclock', 'update_interval': 0.04}</properties>
		<properties format="literal" node_id="9">{'absolute_time': False, 'always_on_top': False, 'antialiased': True, 'auto_line_colors': False, 'autoscale': True, 'background_color': '#FFFFFF', 'decoration_color': '#000000', 'downsampled': False, 'font_size': 10.0, 'initial_dims': [50, 50, 700, 500], 'line_color': '#000000', 'line_width': 0.75, 'marker_color': '#FF0000', 'max_channels': 32, 'metadata': {}, 'nans_as_zero': False, 'no_concatenate': False, 'override_srate': '(use default)', 'plot_markers': True, 'plot_minmax': False, 'savedWidgetGeometry': None, 'scale': 1.0, 'set_breakpoint': False, 'show_toolbar': False, 'stream_name': '(use default)', 'time_range': 5.0, 'title': 'Time series view', 'zero_color': '#7F7F7F', 'zeromean': True}</properties>
		<properties format="literal" node_id="10">{'data_dtype': 'float64', 'data_range_to_stream': 'legacy-warn', 'hitch_probability': 0.0, 'jitter_percent': 5, 'log_progress': False, 'looping': True, 'metadata': {}, 'randseed': 34535, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'speedup': 1.0, 'start_pos': 0.0, 'timestamp_jitter': 0.0, 'timing': 'wallclock', 'update_interval': 0.04}</properties>
		<properties format="pickle" node_id="11">gAN9cQAoWAgAAABtZXRhZGF0YXEBfXECWBEAAAByZXBsYWNlX2lmX2V4aXN0c3EDiVgTAAAAc2F2
ZWRXaWRnZXRHZW9tZXRyeXEEY3NpcApfdW5waWNrbGVfdHlwZQpxBVgMAAAAUHlRdDUuUXRDb3Jl
cQZYCgAAAFFCeXRlQXJyYXlxB0NCAdnQywADAAAAAAbCAAADjAAACCsAAASFAAAGwwAAA7kAAAgq
AAAEhAAAAAAAAAAADwAAAAbDAAADuQAACCoAAASEcQiFcQmHcQpScQtYDgAAAHNldF9icmVha3Bv
aW50cQyJWAcAAABzb3J0aW5ncQ1YBQAAAGlucHV0cQ51Lg==
</properties>
		<properties format="literal" node_id="12">{'force_monotonic': True, 'forget_halftime': 90, 'max_updaterate': 500, 'metadata': {}, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'warmup_samples': -1}</properties>
		<properties format="pickle" node_id="13">gAN9cQAoWAwAAABhbGxvd19kb3VibGVxAYlYDwAAAGNsb3NlX29uX21hcmtlcnECWA8AAABjbG9z
ZS1yZWNvcmRpbmdxA1gNAAAAY2xvdWRfYWNjb3VudHEEWAAAAABxBVgMAAAAY2xvdWRfYnVja2V0
cQZoBVgRAAAAY2xvdWRfY3JlZGVudGlhbHNxB2gFWAoAAABjbG91ZF9ob3N0cQhYBwAAAERlZmF1
bHRxCVgOAAAAY2xvdWRfcGFydHNpemVxCkseWAwAAABkZWxldGVfcGFydHNxC4hYCAAAAGZpbGVu
YW1lcQxYSAAAAHplcm9waGFzZS1kZWppdHRlcmVkLWlpci00b3JkZXItMXRvMjgtZWVnLWFuZC1k
ZWppdHRlcmVkLWV5ZXRyYWNraW5nLnhkZnENWAgAAABtZXRhZGF0YXEOfXEPWAsAAABvdXRwdXRf
cm9vdHEQaAVYGgAAAHByZXNlcnZlX29yaWdpbmFsX21ldGFkYXRhcRGJWAsAAAByZXRyaWV2YWJs
ZXESiVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXETY3NpcApfdW5waWNrbGVfdHlwZQpxFFgMAAAA
UHlRdDUuUXRDb3JlcRVYCgAAAFFCeXRlQXJyYXlxFkNCAdnQywADAAAAAAX8AAACcAAACjAAAATV
AAAF/QAAAp0AAAovAAAE1AAAAAAAAAAADwAAAAX9AAACnQAACi8AAATUcReFcRiHcRlScRpYDQAA
AHNlc3Npb25fbm90ZXNxG2gFWA4AAABzZXRfYnJlYWtwb2ludHEciVgHAAAAdmVyYm9zZXEdiXUu
</properties>
		<properties format="literal" node_id="14">{'data_dtype': 'float64', 'data_range_to_stream': 'legacy-warn', 'hitch_probability': 0.0, 'jitter_percent': 5, 'log_progress': False, 'looping': True, 'metadata': {}, 'randseed': 34535, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'speedup': 1.0, 'start_pos': 0.0, 'timestamp_jitter': 0.0, 'timing': 'wallclock', 'update_interval': 0.04}</properties>
		<properties format="pickle" node_id="15">gAN9cQAoWAgAAABtZXRhZGF0YXEBfXECWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQNjc2lwCl91
bnBpY2tsZV90eXBlCnEEWAwAAABQeVF0NS5RdENvcmVxBVgKAAAAUUJ5dGVBcnJheXEGQ0IB2dDL
AAMAAAAAArIAAAZZAAAGpgAABzoAAAKzAAAGhgAABqUAAAc5AAAAAAAAAAAPAAAAArMAAAaGAAAG
pQAABzlxB4VxCIdxCVJxClgOAAAAc2V0X2JyZWFrcG9pbnRxC4lYBQAAAHZhbHVlcQxYbQAAAEM6
L1VzZXJzL3ZpemxhYl9zdHVkL2lkYXR0MjkwMF9ncjkyL25ldXJvcHlwZS1waXBlbGluZS9MU0xE
YXRhX2Zhc3RfYmxpbmtzVjJfb2ZmbGluZS9MU0xEYXRhX2Zhc3RfYmxpbmtzVjJfMjBxDXUu
</properties>
		<properties format="pickle" node_id="16">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgGAAAAZGVzaWducQNYBgAAAGJ1dHRlcnEEWAsA
AABmcmVxdWVuY2llc3EFXXEGKEsBSxxlWAsAAABpZ25vcmVfbmFuc3EHiVgIAAAAbWV0YWRhdGFx
CH1xCVgEAAAAbW9kZXEKWAgAAABiYW5kcGFzc3ELWBAAAABvZmZsaW5lX2ZpbHRmaWx0cQyIWAUA
AABvcmRlcnENSwRYCQAAAHBhc3NfbG9zc3EOR0AIAAAAAAAAWBMAAABzYXZlZFdpZGdldEdlb21l
dHJ5cQ9jc2lwCl91bnBpY2tsZV90eXBlCnEQWAwAAABQeVF0NS5RdENvcmVxEVgKAAAAUUJ5dGVB
cnJheXESQ0IB2dDLAAMAAAAABrAAAAMiAAAIPQAABPAAAAaxAAADTwAACDwAAATvAAAAAAAAAAAP
AAAABrEAAANPAAAIPAAABO9xE4VxFIdxFVJxFlgOAAAAc2V0X2JyZWFrcG9pbnRxF4lYCgAAAHN0
b3BfYXR0ZW5xGEdASQAAAAAAAHUu
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
            "node1",
            "data",
            "node13",
            "data"
        ],
        [
            "node4",
            "outdata",
            "node2",
            "data"
        ],
        [
            "node2",
            "data",
            "node5",
            "data"
        ],
        [
            "node13",
            "data",
            "node3",
            "data"
        ],
        [
            "node13",
            "data",
            "node17",
            "data"
        ],
        [
            "node3",
            "data",
            "node15",
            "data"
        ],
        [
            "node15",
            "data",
            "node4",
            "data2"
        ],
        [
            "node11",
            "data",
            "node4",
            "data1"
        ],
        [
            "node11",
            "data",
            "node10",
            "data"
        ],
        [
            "node11",
            "data",
            "node12",
            "data1"
        ],
        [
            "node16",
            "data",
            "node5",
            "output_root"
        ],
        [
            "node16",
            "data",
            "node14",
            "output_root"
        ],
        [
            "node8",
            "data",
            "node6",
            "data"
        ],
        [
            "node6",
            "data",
            "node11",
            "data"
        ],
        [
            "node12",
            "outdata",
            "node7",
            "data"
        ],
        [
            "node7",
            "data",
            "node14",
            "data"
        ],
        [
            "node17",
            "data",
            "node9",
            "data"
        ],
        [
            "node9",
            "data",
            "node12",
            "data2"
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
                    "customized": true,
                    "type": "StringPort",
                    "value": "C:/Users/vizlab_stud/idatt2900_gr92/neuropype-pipeline/LSLData_fast_blinksV2/LSLData_fast_blinksV2_20/raw-eeg.xdf"
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
            "uuid": "4882e169-9ea4-49d2-b049-ee5a4678f828"
        },
        "node10": {
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
                    "value": 8
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
            "uuid": "882be015-6ce9-4447-a2e4-1e438c5958f8"
        },
        "node11": {
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
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
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
            "uuid": "ee3f478d-761b-46c0-914d-704bd7f0e2d2"
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
            "uuid": "7f2c83de-5852-45ec-b928-97a9f563422a"
        },
        "node13": {
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
            "uuid": "67fa89e4-2bb0-4a8a-be3c-b084c007f751"
        },
        "node14": {
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
                    "value": "zerophase-dejittered-iir-4order-1to28-eeg-and-dejittered-eyetracking.xdf"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "output_root": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "C:/Users/vizlab_stud/idatt2900_gr92/neuropype-pipeline/LSLData_fast_blinksV2_offline/LSLData_fast_blinksV2_20"
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
            "uuid": "abcaa821-2495-4f49-90e8-204a16e1c1a2"
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
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
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
            "uuid": "45294263-66c4-475f-9fd9-db7a9d4de313"
        },
        "node16": {
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
                    "value": "C:/Users/vizlab_stud/idatt2900_gr92/neuropype-pipeline/LSLData_fast_blinksV2_offline/LSLData_fast_blinksV2_20"
                }
            },
            "uuid": "df880262-dea3-4d52-a815-99a69bde2c1b"
        },
        "node17": {
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
                        1,
                        28
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
            "uuid": "a1ac81f4-13cc-44e9-9caa-880e6a5fa277"
        },
        "node2": {
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
                    "value": 120
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
            "uuid": "d7059bb8-00c1-4a71-ad32-ab8329263e49"
        },
        "node3": {
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
            "uuid": "e082e490-8250-495e-b757-1dd557641b25"
        },
        "node4": {
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
            "uuid": "3c61251e-d45d-4bb9-a2c3-7c3dca4470af"
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
                    "value": "zerophase-dejittered-iir-4order-0.75to5-eeg-and-dejittered-eyetracking.xdf"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "output_root": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "C:/Users/vizlab_stud/idatt2900_gr92/neuropype-pipeline/LSLData_fast_blinksV2_offline/LSLData_fast_blinksV2_20"
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
            "uuid": "d37bc6bb-b9a2-427b-8c57-2e3d8fcdc4de"
        },
        "node6": {
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
            "uuid": "5977a75a-1c66-46b0-be7f-e48f95ac0296"
        },
        "node7": {
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
                    "value": 120
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
            "uuid": "a357a75e-bcf6-4cee-83b1-8755518b4c83"
        },
        "node8": {
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
                    "value": "C:/Users/vizlab_stud/idatt2900_gr92/neuropype-pipeline/LSLData_fast_blinksV2/LSLData_fast_blinksV2_20/gaze-and-blinking.xdf"
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
            "uuid": "c64eca97-2ec6-4df8-b96a-8511935f6b94"
        },
        "node9": {
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
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
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
            "uuid": "8886e51c-e312-49d6-8a2d-60dda623443f"
        }
    },
    "version": 1.1
}</patch>
</scheme>
