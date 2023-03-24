<?xml version='1.0' encoding='utf-8'?>
<scheme description="" title="test" version="2.0">
	<nodes>
		<node id="0" name="Import File" position="(312.0, 312.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportfile.OWImportFile" title="Import File" uuid="264b2d12-5bce-486e-9139-209c4844fb6b" version="1.2.1" />
		<node id="1" name="Stream Data" position="(508.0, 322.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owstreamdata.OWStreamData" title="Stream Data" uuid="6e221dfd-2f18-44b5-b222-78e47ddcc796" version="1.2.1" />
		<node id="2" name="LSL Output" position="(667.0, 324.0)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output" uuid="bd810821-b11a-4c82-95cd-9b6d8c6ac8b9" version="1.4.3" />
		<node id="3" name="Inspect Data" position="(623.0, 197.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owinspectdata.OWInspectData" title="Inspect Data" uuid="836dccb7-8217-4ae3-86a1-a54db10e3432" version="2.2.4" />
		<node id="4" name="LSL Input" position="(315.0, 451.0)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="LSL Input" uuid="4500fc67-c16d-475e-ad9b-07fba1e203a1" version="1.3.6" />
		<node id="5" name="Inspect Data" position="(494.0, 442.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owinspectdata.OWInspectData" title="Inspect Data (1)" uuid="327f618f-0e56-4efa-a0a1-a08eb30832e7" version="2.2.4" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="1" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="1" sink_channel="Data" sink_node_id="2" source_channel="Data" source_node_id="1" />
		<link enabled="true" id="2" sink_channel="Data" sink_node_id="3" source_channel="Data" source_node_id="1" />
		<link enabled="true" id="3" sink_channel="Data" sink_node_id="5" source_channel="Data" source_node_id="4" />
	</links>
	<annotations />
	<thumbnail />
	<node_properties>
		<properties format="pickle" node_id="0">gAN9cQAoWBgAAABhbGxvd19pbnNlY3VyZV9maWxldHlwZXNxAYlYDQAAAGNsb3VkX2FjY291bnRx
AlgAAAAAcQNYDAAAAGNsb3VkX2J1Y2tldHEEaANYEQAAAGNsb3VkX2NyZWRlbnRpYWxzcQVoA1gK
AAAAY2xvdWRfaG9zdHEGWAcAAABEZWZhdWx0cQdYCAAAAGZpbGVuYW1lcQhYwQAAAEM6L1VzZXJz
L3hyYXkyL09uZURyaXZlL0RvY3VtZW50cy9OVE5VL0RhdGFJbmcyMDIzL3MyMDIzL2JhL25ldXJv
cHlwZS1waXBlbGluZS9qaXR0ZXIvZGF0YS9CQ0lTcGVsbGVyVjUvQkNJU3BlbGxlclY1OC4xOF8y
L2Rlaml0dGVyZWQtc2hpZnRlZDQzbXMtZGVjaW1hdGUyLWVlZy1paXItYW5kLWRlaml0dGVyZWQt
dW5pdHktZnJlcS54ZGZxCVgLAAAAbG9hZF9ldmVudHNxCohYDAAAAGxvYWRfc2lnbmFsc3ELiFgI
AAAAbWV0YWRhdGFxDH1xDVgOAAAAcmV0YWluX3N0cmVhbXNxDlgNAAAAKHVzZSBkZWZhdWx0KXEP
WBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cRBjc2lwCl91bnBpY2tsZV90eXBlCnERWAwAAABQeVF0
NS5RdENvcmVxElgKAAAAUUJ5dGVBcnJheXETQ0IB2dDLAAMAAAAAAwsAAAE6AAAEdAAAArgAAAMM
AAABWQAABHMAAAK3AAAAAAAAAAAHgAAAAwwAAAFZAAAEcwAAArdxFIVxFYdxFlJxF1gIAAAAc2Vn
bWVudHNxGGgPWA4AAABzZXRfYnJlYWtwb2ludHEZiVgQAAAAc2lnbmFsX2F1dG9zY2FsZXEaiFgM
AAAAc3RpbV9jaGFubmVscRtoA1gLAAAAdGltZV9ib3VuZHNxHGgPWA8AAAB1c2Vfc3RyZWFtbmFt
ZXNxHYl1Lg==
</properties>
		<properties format="literal" node_id="1">{'data_dtype': 'float64', 'hitch_probability': 0.0, 'jitter_percent': 5, 'log_progress': False, 'looping': True, 'metadata': {}, 'randseed': 34535, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'speedup': 1.0, 'start_pos': 0.0, 'timestamp_jitter': 0.0, 'timing': 'wallclock', 'update_interval': 0.04}</properties>
		<properties format="pickle" node_id="2">gAN9cQAoWAkAAABjaHVua19sZW5xAUsAWBUAAABpZ25vcmVfc2lnbmFsX2NoYW5nZWRxAolYEwAA
AGtlZXBfc2luZ2xldG9uX2F4ZXNxA4lYDAAAAG1hcmtlcl9maWVsZHEEWAYAAABNYXJrZXJxBVgL
AAAAbWFya2VyX25hbWVxBlgRAAAAT3V0U3RyZWFtLW1hcmtlcnNxB1gQAAAAbWFya2VyX3NvdXJj
ZV9pZHEIWAAAAABxCVgMAAAAbWF4X2J1ZmZlcmVkcQpLPFgIAAAAbWV0YWRhdGFxC31xDFgXAAAA
bnVtZXJpY19sYWJlbF9wcmVjaXNpb25xDUsBWBgAAABudW1lcmljX21hcmtlcl9wcmVjaXNpb25x
DksDWBcAAAByZXNldF9pZl9sYWJlbHNfY2hhbmdlZHEPiVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRy
eXEQY3NpcApfdW5waWNrbGVfdHlwZQpxEVgMAAAAUHlRdDUuUXRDb3JlcRJYCgAAAFFCeXRlQXJy
YXlxE0NCAdnQywADAAAAAAMLAAABAgAABHQAAALvAAADDAAAASEAAARzAAAC7gAAAAAAAAAAB4AA
AAMMAAABIQAABHMAAALucRSFcRWHcRZScRdYDAAAAHNlbmRfbWFya2Vyc3EYiVgJAAAAc2VwYXJh
dG9ycRlYAQAAAC1xGlgOAAAAc2V0X2JyZWFrcG9pbnRxG4lYCQAAAHNvdXJjZV9pZHEcaAlYBQAA
AHNyYXRlcR1YDQAAACh1c2UgZGVmYXVsdClxHlgLAAAAc3RyZWFtX25hbWVxH1gEAAAAVGVzdHEg
WAsAAABzdHJlYW1fdHlwZXEhWAQAAABUZXN0cSJYEwAAAHVzZV9kYXRhX3RpbWVzdGFtcHNxI4hY
FgAAAHVzZV9udW1weV9vcHRpbWl6YXRpb25xJIl1Lg==
</properties>
		<properties format="literal" node_id="3">{'always_on_top': True, 'auto_close': True, 'col_axis': 'time', 'decimals': 6, 'every_n_ticks': 1, 'fewer_buttons': False, 'font_size': 10, 'initial_position': [20, 50, 500, 400], 'metadata': {}, 'row_axis': 'space', 'savedWidgetGeometry': None, 'set_breakpoint': False, 'show_axes_table': True, 'show_data_table': True, 'show_markers_table': True, 'show_max_columns': 20, 'show_max_values': 50, 'show_streams_table': True, 'stream_name': '(use default)', 'window_title': 'Inspect Data Packet'}</properties>
		<properties format="pickle" node_id="4">gAN9cQAoWA0AAABjaGFubmVsX25hbWVzcQFdcQJYCgAAAGRhdGFfZHR5cGVxA1gHAAAAZmxvYXQ2
NHEEWAsAAABkaWFnbm9zdGljc3EFiVgTAAAAZXhjbHVkZV9kZXNjX2ZpZWxkc3EGXXEHWAwAAABt
YXJrZXJfcXVlcnlxCFgAAAAAcQlYDAAAAG1heF9ibG9ja2xlbnEKTQAEWAoAAABtYXhfYnVmbGVu
cQtLHlgMAAAAbWF4X2NodW5rbGVucQxLAFgIAAAAbWV0YWRhdGFxDX1xDlgMAAAAbm9taW5hbF9y
YXRlcQ9YDQAAACh1c2UgZGVmYXVsdClxEFgJAAAAb21pdF9kZXNjcRGJWA8AAABwcmVhbGxvY19i
dWZmZXJxEohYDgAAAHByb2NfY2xvY2tzeW5jcROIWA0AAABwcm9jX2Rlaml0dGVycRSJWA8AAABw
cm9jX21vbm90b25pemVxFYlYDwAAAHByb2NfdGhyZWFkc2FmZXEWiVgFAAAAcXVlcnlxF1gKAAAA
bmFtZT0nQ0NBJ3EYWAcAAAByZWNvdmVycRmIWBQAAAByZXNvbHZlX21pbmltdW1fdGltZXEaRz/g
AAAAAAAAWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cRtjc2lwCl91bnBpY2tsZV90eXBlCnEcWAwA
AABQeVF0NS5RdENvcmVxHVgKAAAAUUJ5dGVBcnJheXEeQ0IB2dDLAAMAAAAAAwwAAAF3AAAEcwAA
ApkAAAMMAAABdwAABHMAAAKZAAAAAAAAAAAHgAAAAwwAAAF3AAAEcwAAAplxH4VxIIdxIVJxIlgO
AAAAc2V0X2JyZWFrcG9pbnRxI4l1Lg==
</properties>
		<properties format="literal" node_id="5">{'always_on_top': True, 'auto_close': True, 'col_axis': 'time', 'decimals': 6, 'every_n_ticks': 1, 'fewer_buttons': False, 'font_size': 10, 'initial_position': [20, 50, 500, 400], 'metadata': {}, 'row_axis': 'space', 'savedWidgetGeometry': None, 'set_breakpoint': False, 'show_axes_table': True, 'show_data_table': True, 'show_markers_table': True, 'show_max_columns': 20, 'show_max_values': 50, 'show_streams_table': True, 'stream_name': '(use default)', 'window_title': 'Inspect Data Packet'}</properties>
	</node_properties>
	<patch />
</scheme>
