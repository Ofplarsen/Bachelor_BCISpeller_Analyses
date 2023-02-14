<?xml version='1.0' encoding='utf-8'?>
<scheme description="" title="EEGAndEyeTrackerPlayback" version="2.0">
	<nodes>
		<node id="0" name="Stream Data" position="(321.0, 179.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owstreamdata.OWStreamData" title="Stream Data" uuid="e4d77308-492f-40eb-82f5-ebd6f17c44a6" version="1.3.0" />
		<node id="1" name="LSL Output" position="(477.0, 176.0)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output" uuid="d852b94c-d923-4078-a5a0-87124a76c941" version="1.4.3" />
		<node id="2" name="LSL Input" position="(539.0, 678.0)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="LSL Input" uuid="ea6855dc-4364-4b5f-8e26-e624a3aa7adf" version="1.4.0" />
		<node id="3" name="Print To Console" position="(631.0, 815.0)" project_name="NeuroPype" qualified_name="widgets.diagnostics.owprinttoconsole.OWPrintToConsole" title="Print To Console" uuid="9e1eabd3-ff21-49b0-8721-3b6342286b26" version="1.1.0" />
		<node id="4" name="Import CSV" position="(175.0, 181.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportcsv.OWImportCSV" title="Import CSV" uuid="ced786db-6f7b-4a3a-a5db-d715c8f16a80" version="1.2.1" />
		<node id="5" name="Import File" position="(168.0, 69.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportfile.OWImportFile" title="Import File" uuid="93abb1a2-fc69-400c-99c9-9ac30fbf538e" version="1.2.1" />
		<node id="6" name="Import SET" position="(180.0, 318.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportset.OWImportSET" title="Import SET" uuid="ca57a900-48aa-46d4-b555-cd73b6708ba7" version="1.2.2" />
		<node id="7" name="Import XDF" position="(177.0, 448.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportxdf.OWImportXDF" title="Import XDF" uuid="4b56bf9c-9a43-4db1-9ffb-d0107fd2e0e0" version="1.4.1" />
		<node id="8" name="Inspect Packet" position="(738.0, 580.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owinspectpacket.OWInspectPacket" title="Inspect Packet" uuid="c7165617-8f84-46f3-880b-b828c66529ab" version="3.0.1" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="1" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="1" sink_channel="Data" sink_node_id="0" source_channel="Data" source_node_id="7" />
		<link enabled="true" id="2" sink_channel="Data" sink_node_id="3" source_channel="Data" source_node_id="2" />
		<link enabled="true" id="3" sink_channel="Data" sink_node_id="8" source_channel="Data" source_node_id="2" />
	</links>
	<annotations />
	<thumbnail />
	<node_properties>
		<properties format="pickle" node_id="0">gAN9cQAoWAoAAABkYXRhX2R0eXBlcQFYBwAAAGZsb2F0NjRxAlgUAAAAZGF0YV9yYW5nZV90b19z
dHJlYW1xA1gLAAAAbGVnYWN5LXdhcm5xBFgRAAAAaGl0Y2hfcHJvYmFiaWxpdHlxBUcAAAAAAAAA
AFgOAAAAaml0dGVyX3BlcmNlbnRxBksFWAwAAABsb2dfcHJvZ3Jlc3NxB4lYBwAAAGxvb3Bpbmdx
CIhYCAAAAG1ldGFkYXRhcQl9cQpYCAAAAHJhbmRzZWVkcQtN54ZYEwAAAHNhdmVkV2lkZ2V0R2Vv
bWV0cnlxDGNzaXAKX3VucGlja2xlX3R5cGUKcQ1YDAAAAFB5UXQ1LlF0Q29yZXEOWAoAAABRQnl0
ZUFycmF5cQ9DQgHZ0MsAAwAAAAAI2AAAAuYAAArLAAAFFAAACNkAAAMTAAAKygAABRMAAAAAAAAA
AA8AAAAI2QAAAxMAAArKAAAFE3EQhXERh3ESUnETWA4AAABzZXRfYnJlYWtwb2ludHEUiVgHAAAA
c3BlZWR1cHEVRz/wAAAAAAAAWAkAAABzdGFydF9wb3NxFkcAAAAAAAAAAFgQAAAAdGltZXN0YW1w
X2ppdHRlcnEXRwAAAAAAAAAAWAYAAAB0aW1pbmdxGFgJAAAAd2FsbGNsb2NrcRlYDwAAAHVwZGF0
ZV9pbnRlcnZhbHEaRz+keuFHrhR7dS4=
</properties>
		<properties format="pickle" node_id="1">gAN9cQAoWAkAAABjaHVua19sZW5xAUsAWBUAAABpZ25vcmVfc2lnbmFsX2NoYW5nZWRxAolYEwAA
AGtlZXBfc2luZ2xldG9uX2F4ZXNxA4lYDAAAAG1hcmtlcl9maWVsZHEEWAYAAABNYXJrZXJxBVgL
AAAAbWFya2VyX25hbWVxBlgRAAAAT3V0U3RyZWFtLW1hcmtlcnNxB1gQAAAAbWFya2VyX3NvdXJj
ZV9pZHEIWAAAAABxCVgMAAAAbWF4X2J1ZmZlcmVkcQpLPFgIAAAAbWV0YWRhdGFxC31xDFgXAAAA
bnVtZXJpY19sYWJlbF9wcmVjaXNpb25xDUsBWBgAAABudW1lcmljX21hcmtlcl9wcmVjaXNpb25x
DksDWBcAAAByZXNldF9pZl9sYWJlbHNfY2hhbmdlZHEPiVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRy
eXEQY3NpcApfdW5waWNrbGVfdHlwZQpxEVgMAAAAUHlRdDUuUXRDb3JlcRJYCgAAAFFCeXRlQXJy
YXlxE0NCAdnQywADAAAAAAa0AAACxAAACDkAAAV5AAAGtAAAAsQAAAg5AAAFeQAAAAAAAAAADwAA
AAa0AAACxAAACDkAAAV5cRSFcRWHcRZScRdYDAAAAHNlbmRfbWFya2Vyc3EYiVgJAAAAc2VwYXJh
dG9ycRlYAQAAAC1xGlgOAAAAc2V0X2JyZWFrcG9pbnRxG4lYCQAAAHNvdXJjZV9pZHEcaAlYBQAA
AHNyYXRlcR1YDQAAACh1c2UgZGVmYXVsdClxHlgLAAAAc3RyZWFtX25hbWVxH1gOAAAAUGxheWJh
Y2tTdHJlYW1xIFgLAAAAc3RyZWFtX3R5cGVxIVgIAAAAUGxheWJhY2txIlgTAAAAdXNlX2RhdGFf
dGltZXN0YW1wc3EjiFgWAAAAdXNlX251bXB5X29wdGltaXphdGlvbnEkiXUu
</properties>
		<properties format="pickle" node_id="2">gAN9cQAoWA0AAABjaGFubmVsX25hbWVzcQFdcQJYCgAAAGRhdGFfZHR5cGVxA1gHAAAAZmxvYXQ2
NHEEWAsAAABkaWFnbm9zdGljc3EFiVgTAAAAZXhjbHVkZV9kZXNjX2ZpZWxkc3EGXXEHWA4AAABs
b2NhbGhvc3Rfb25seXEIiVgMAAAAbWFya2VyX3F1ZXJ5cQlYAAAAAHEKWAwAAABtYXhfYmxvY2ts
ZW5xC00ABFgKAAAAbWF4X2J1ZmxlbnEMSx5YDAAAAG1heF9jaHVua2xlbnENSwBYCAAAAG1ldGFk
YXRhcQ59cQ9YDAAAAG5vbWluYWxfcmF0ZXEQWA0AAAAodXNlIGRlZmF1bHQpcRFYCQAAAG9taXRf
ZGVzY3ESiVgPAAAAcHJlYWxsb2NfYnVmZmVycROIWA4AAABwcm9jX2Nsb2Nrc3luY3EUiFgNAAAA
cHJvY19kZWppdHRlcnEViVgPAAAAcHJvY19tb25vdG9uaXplcRaJWA8AAABwcm9jX3RocmVhZHNh
ZmVxF4lYBQAAAHF1ZXJ5cRhYFQAAAG5hbWU9J1BsYXliYWNrU3RyZWFtJ3EZWAcAAAByZWNvdmVy
cRqIWBQAAAByZXNvbHZlX21pbmltdW1fdGltZXEbRz/gAAAAAAAAWBMAAABzYXZlZFdpZGdldEdl
b21ldHJ5cRxjc2lwCl91bnBpY2tsZV90eXBlCnEdWAwAAABQeVF0NS5RdENvcmVxHlgKAAAAUUJ5
dGVBcnJheXEfQ0IB2dDLAAMAAAAACHQAAAKSAAAKDgAABYMAAAh1AAACvwAACg0AAAWCAAAAAAAA
AAAPAAAACHUAAAK/AAAKDQAABYJxIIVxIYdxIlJxI1gOAAAAc2V0X2JyZWFrcG9pbnRxJIl1Lg==
</properties>
		<properties format="literal" node_id="3">{'metadata': {}, 'only_nonempty': True, 'print_channel': False, 'print_compact': True, 'print_data': False, 'print_markers': False, 'print_props': False, 'print_streams': [], 'print_time': False, 'print_trial': False, 'savedWidgetGeometry': None, 'set_breakpoint': False}</properties>
		<properties format="pickle" node_id="4">gAN9cQAoWA0AAABjbG91ZF9hY2NvdW50cQFYAAAAAHECWAwAAABjbG91ZF9idWNrZXRxA2gCWBEA
AABjbG91ZF9jcmVkZW50aWFsc3EEaAJYCgAAAGNsb3VkX2hvc3RxBVgHAAAARGVmYXVsdHEGWBAA
AABkYXRhX3N0cmVhbV9uYW1lcQdYAwAAAGVlZ3EIWAkAAABkZWxpbWl0ZXJxCVgBAAAALHEKWA4A
AABlbWl0X2VhY2hfdGlja3ELiVgPAAAAZXhjbHVkZV9jb2x1bW5zcQxdcQ1YCAAAAGZpbGVuYW1l
cQ5YNwAAAEM6L1VzZXJzL3ZpemxhYl9zdHVkL2lkYXR0MjkwMF9ncjkyL0xTTERhdGEvcmF3X2Vl
Zy5jc3ZxD1gRAAAAaWdub3JlX2VtcHR5X3Jvd3NxEIhYDwAAAGluY2x1ZGVfY29sdW1uc3ERXXES
WBQAAABpbnN0YW5jZV9jb2x1bW5fbmFtZXETaAJYDQAAAG1hcmtlcl9jb2x1bW5xFFgNAAAAKHVz
ZSBkZWZhdWx0KXEVWBIAAABtYXJrZXJfY29sdW1uX25hbWVxFmgCWAgAAABtZXRhZGF0YXEXfXEY
WBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cRljc2lwCl91bnBpY2tsZV90eXBlCnEaWAwAAABQeVF0
NS5RdENvcmVxG1gKAAAAUUJ5dGVBcnJheXEcQ0IB2dDLAAMAAAAABrQAAAKgAAAIOQAABXEAAAa1
AAACzQAACDgAAAVwAAAAAAAAAAAPAAAABrUAAALNAAAIOAAABXBxHYVxHodxH1JxIFgOAAAAc2V0
X2JyZWFrcG9pbnRxIYlYEAAAAHRpbWVzdGFtcF9jb2x1bW5xIlgNAAAAKHVzZSBkZWZhdWx0KXEj
WBUAAAB0aW1lc3RhbXBfY29sdW1uX25hbWVxJGgCWA8AAAB0aW1lc3RhbXBfdW5pdHNxJVgHAAAA
c2Vjb25kc3EmdS4=
</properties>
		<properties format="pickle" node_id="5">gAN9cQAoWBgAAABhbGxvd19pbnNlY3VyZV9maWxldHlwZXNxAYlYDQAAAGNsb3VkX2FjY291bnRx
AlgAAAAAcQNYDAAAAGNsb3VkX2J1Y2tldHEEaANYEQAAAGNsb3VkX2NyZWRlbnRpYWxzcQVoA1gK
AAAAY2xvdWRfaG9zdHEGWAcAAABEZWZhdWx0cQdYCAAAAGZpbGVuYW1lcQhYFAAAAHNhbXBsZS1n
YXplLWRhdGEueGRmcQlYCwAAAGxvYWRfZXZlbnRzcQqIWAwAAABsb2FkX3NpZ25hbHNxC4hYCAAA
AG1ldGFkYXRhcQx9cQ1YDgAAAHJldGFpbl9zdHJlYW1zcQ5YDQAAACh1c2UgZGVmYXVsdClxD1gT
AAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEQY3NpcApfdW5waWNrbGVfdHlwZQpxEVgMAAAAUHlRdDUu
UXRDb3JlcRJYCgAAAFFCeXRlQXJyYXlxE0NCAdnQywADAAAAAAbCAAAC1gAACCsAAAU7AAAGwwAA
AwMAAAgqAAAFOgAAAAAAAAAADwAAAAbDAAADAwAACCoAAAU6cRSFcRWHcRZScRdYCAAAAHNlZ21l
bnRzcRhYDQAAACh1c2UgZGVmYXVsdClxGVgOAAAAc2V0X2JyZWFrcG9pbnRxGolYEAAAAHNpZ25h
bF9hdXRvc2NhbGVxG4hYDAAAAHN0aW1fY2hhbm5lbHEcaANYCwAAAHRpbWVfYm91bmRzcR1YDQAA
ACh1c2UgZGVmYXVsdClxHlgPAAAAdXNlX3N0cmVhbW5hbWVzcR+JdS4=
</properties>
		<properties format="pickle" node_id="6">gAN9cQAoWA0AAABjbG91ZF9hY2NvdW50cQFYAAAAAHECWAwAAABjbG91ZF9idWNrZXRxA2gCWBEA
AABjbG91ZF9jcmVkZW50aWFsc3EEaAJYCgAAAGNsb3VkX2hvc3RxBVgHAAAARGVmYXVsdHEGWAgA
AABmaWxlbmFtZXEHWBIAAABFbW90aW9uVmFsZW5jZS5zZXRxCFgIAAAAbWV0YWRhdGFxCX1xClgT
AAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXELY3NpcApfdW5waWNrbGVfdHlwZQpxDFgMAAAAUHlRdDUu
UXRDb3JlcQ1YCgAAAFFCeXRlQXJyYXlxDkNCAdnQywADAAAAAAbCAAADWgAACCsAAAS4AAAGwwAA
A4cAAAgqAAAEtwAAAAAAAAAADwAAAAbDAAADhwAACCoAAAS3cQ+FcRCHcRFScRJYDgAAAHNldF9i
cmVha3BvaW50cROJdS4=
</properties>
		<properties format="pickle" node_id="7">gAN9cQAoWA0AAABjbG91ZF9hY2NvdW50cQFYAAAAAHECWAwAAABjbG91ZF9idWNrZXRxA2gCWBEA
AABjbG91ZF9jcmVkZW50aWFsc3EEaAJYCgAAAGNsb3VkX2hvc3RxBVgHAAAARGVmYXVsdHEGWAgA
AABmaWxlbmFtZXEHWEMAAABDOi9Vc2Vycy92aXpsYWJfc3R1ZC9pZGF0dDI5MDBfZ3I5Mi9MU0xE
YXRhL2VlZy1hbmQtZXlldHJhY2tpbmcueGRmcQhYEwAAAGhhbmRsZV9jbG9ja19yZXNldHNxCYhY
EQAAAGhhbmRsZV9jbG9ja19zeW5jcQqIWBUAAABoYW5kbGVfaml0dGVyX3JlbW92YWxxC4hYDgAA
AG1heF9tYXJrZXJfbGVucQxYDQAAACh1c2UgZGVmYXVsdClxDVgIAAAAbWV0YWRhdGFxDn1xD1gS
AAAAcmVvcmRlcl90aW1lc3RhbXBzcRCJWA4AAAByZXRhaW5fc3RyZWFtc3ERaA1YEwAAAHNhdmVk
V2lkZ2V0R2VvbWV0cnlxEmNzaXAKX3VucGlja2xlX3R5cGUKcRNYDAAAAFB5UXQ1LlF0Q29yZXEU
WAoAAABRQnl0ZUFycmF5cRVDQgHZ0MsAAwAAAAAGwgAAAtsAAAgrAAAFNgAABsMAAAMIAAAIKgAA
BTUAAAAAAAAAAA8AAAAGwwAAAwgAAAgqAAAFNXEWhXEXh3EYUnEZWA4AAABzZXRfYnJlYWtwb2lu
dHEaiVgLAAAAdXNlX2NhY2hpbmdxG4lYDwAAAHVzZV9zdHJlYW1uYW1lc3EciVgHAAAAdmVyYm9z
ZXEdiXUu
</properties>
		<properties format="literal" node_id="8">{'always_on_top': True, 'col_axis': 'time', 'decimals': 6, 'every_n_ticks': 1, 'fewer_buttons': False, 'font_size': 10, 'initial_position': [20, 50, 500, 400], 'metadata': {}, 'row_axis': 'space', 'savedWidgetGeometry': None, 'set_breakpoint': False, 'show_axes_table': True, 'show_data_table': True, 'show_markers_table': False, 'show_max_columns': 20, 'show_max_values': 50, 'show_streams_table': False, 'stream_name': '(use default)', 'verbose': True, 'window_title': 'Inspect Data Packet'}</properties>
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
            "node2",
            "data"
        ],
        [
            "node8",
            "data",
            "node1",
            "data"
        ],
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
        ]
    ],
    "nodes": {
        "node1": {
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
            "uuid": "e4d77308-492f-40eb-82f5-ebd6f17c44a6"
        },
        "node2": {
            "class": "LSLOutput",
            "module": "neuropype.nodes.network.LSLOutput",
            "params": {
                "chunk_len": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "ignore_signal_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "keep_singleton_axes": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Marker"
                },
                "marker_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "OutStream-markers"
                },
                "marker_source_id": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "max_buffered": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 60
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "numeric_label_precision": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1
                },
                "numeric_marker_precision": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 3
                },
                "reset_if_labels_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "send_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "separator": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "-"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "source_id": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "stream_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "PlaybackStream"
                },
                "stream_type": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "Playback"
                },
                "use_data_timestamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "use_numpy_optimization": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "d852b94c-d923-4078-a5a0-87124a76c941"
        },
        "node3": {
            "class": "LSLInput",
            "module": "neuropype.nodes.network.LSLInput",
            "params": {
                "channel_names": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        "LiveAmpSN-056309-0553-Fp1",
                        "LiveAmpSN-056309-0553-Fz",
                        "LiveAmpSN-056309-0553-F3",
                        "LiveAmpSN-056309-0553-F7",
                        "LiveAmpSN-056309-0553-F9",
                        "LiveAmpSN-056309-0553-FC5",
                        "LiveAmpSN-056309-0553-FC1",
                        "LiveAmpSN-056309-0553-C3",
                        "LiveAmpSN-056309-0553-T7",
                        "LiveAmpSN-056309-0553-CP5",
                        "LiveAmpSN-056309-0553-CP1",
                        "LiveAmpSN-056309-0553-Pz",
                        "LiveAmpSN-056309-0553-P3",
                        "LiveAmpSN-056309-0553-P7",
                        "LiveAmpSN-056309-0553-P9",
                        "LiveAmpSN-056309-0553-O1",
                        "LiveAmpSN-056309-0553-Oz",
                        "LiveAmpSN-056309-0553-O2",
                        "LiveAmpSN-056309-0553-P10",
                        "LiveAmpSN-056309-0553-P8",
                        "LiveAmpSN-056309-0553-P4",
                        "LiveAmpSN-056309-0553-CP2",
                        "LiveAmpSN-056309-0553-CP6",
                        "LiveAmpSN-056309-0553-T8",
                        "LiveAmpSN-056309-0553-C4",
                        "LiveAmpSN-056309-0553-Cz",
                        "LiveAmpSN-056309-0553-FC2",
                        "LiveAmpSN-056309-0553-FC6",
                        "LiveAmpSN-056309-0553-F10",
                        "LiveAmpSN-056309-0553-F8",
                        "LiveAmpSN-056309-0553-F4",
                        "LiveAmpSN-056309-0553-Fp2",
                        "LiveAmpSN-056309-0553-ACC_X",
                        "LiveAmpSN-056309-0553-ACC_Y",
                        "LiveAmpSN-056309-0553-ACC_Z",
                        "3531a346d187a0276b326a50c49417dc-x_direction",
                        "3531a346d187a0276b326a50c49417dc-y_direction",
                        "3531a346d187a0276b326a50c49417dc-z_direction",
                        "3531a346d187a0276b326a50c49417dc-left_blink",
                        "3531a346d187a0276b326a50c49417dc-right_blink",
                        "3531a346d187a0276b326a50c49417dc-both_blink"
                    ]
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
                    "value": "name='PlaybackStream'"
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
                }
            },
            "uuid": "ea6855dc-4364-4b5f-8e26-e624a3aa7adf"
        },
        "node4": {
            "class": "PrintToConsole",
            "module": "neuropype.nodes.diagnostics.PrintToConsole",
            "params": {
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "only_nonempty": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "print_channel": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "print_compact": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "print_data": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "print_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "print_props": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "print_streams": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "print_time": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "print_trial": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "9e1eabd3-ff21-49b0-8721-3b6342286b26"
        },
        "node5": {
            "class": "ImportCSV",
            "module": "neuropype.nodes.file_system.ImportCSV",
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
                "data_stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "eeg"
                },
                "delimiter": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ","
                },
                "emit_each_tick": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "exclude_columns": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "C:/Users/vizlab_stud/idatt2900_gr92/LSLData/raw_eeg.csv"
                },
                "ignore_empty_rows": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "include_columns": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "instance_column_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "marker_column": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "marker_column_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
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
                "timestamp_column": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "timestamp_column_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "timestamp_units": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "seconds"
                }
            },
            "uuid": "ced786db-6f7b-4a3a-a5db-d715c8f16a80"
        },
        "node6": {
            "class": "ImportFile",
            "module": "neuropype.nodes.file_system.ImportFile",
            "params": {
                "allow_insecure_filetypes": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
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
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "sample-gaze-data.xdf"
                },
                "load_events": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "load_signals": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "retain_streams": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "segments": {
                    "customized": false,
                    "type": "ListPort",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "signal_autoscale": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "stim_channel": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "time_bounds": {
                    "customized": false,
                    "type": "ListPort",
                    "value": null
                },
                "use_streamnames": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "93abb1a2-fc69-400c-99c9-9ac30fbf538e"
        },
        "node7": {
            "class": "ImportSET",
            "module": "neuropype.nodes.file_system.ImportSET",
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
                    "value": "EmotionValence.set"
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
            "uuid": "ca57a900-48aa-46d4-b555-cd73b6708ba7"
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
                    "value": "C:/Users/vizlab_stud/idatt2900_gr92/LSLData/eeg-and-eyetracking.xdf"
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
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "4b56bf9c-9a43-4db1-9ffb-d0107fd2e0e0"
        },
        "node9": {
            "class": "InspectPacket",
            "module": "neuropype.nodes.visualization.InspectPacket",
            "params": {
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "col_axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "time"
                },
                "decimals": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 6
                },
                "every_n_ticks": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1
                },
                "fewer_buttons": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "font_size": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 10
                },
                "initial_position": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        20,
                        50,
                        500,
                        400
                    ]
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "row_axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "space"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "show_axes_table": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "show_data_table": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "show_markers_table": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "show_max_columns": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 20
                },
                "show_max_values": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 0
                },
                "show_streams_table": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "playback"
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "window_title": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Inspect Data Packet"
                }
            },
            "uuid": "c7165617-8f84-46f3-880b-b828c66529ab"
        }
    },
    "version": 1.1
}</patch>
</scheme>
