<?xml version='1.0' encoding='utf-8'?>
<scheme description="" title="EEGAndEyeTrackerPlayback" version="2.0">
	<nodes>
		<node id="0" name="Stream Data" position="(366.0, 447.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owstreamdata.OWStreamData" title="Stream Data" uuid="1ad00b73-42f0-42d4-bcd5-54c406f77c59" version="1.2.1" />
		<node id="1" name="LSL Output" position="(522.0, 444.0)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output" uuid="4bdd3433-d698-4002-ac13-d836b5ea0181" version="1.4.3" />
		<node id="2" name="LSL Input" position="(927.0, 513.0)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="LSL Input" uuid="7701e74e-8d91-4933-bf32-899d1a2c429d" version="1.3.6" />
		<node id="3" name="Print To Console" position="(1019.0, 650.0)" project_name="NeuroPype" qualified_name="widgets.diagnostics.owprinttoconsole.OWPrintToConsole" title="Print To Console" uuid="1a302bcf-a868-41d3-a1cf-7e0578fdf802" version="1.1.0" />
		<node id="4" name="Import XDF" position="(177.0, 448.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportxdf.OWImportXDF" title="Import XDF" uuid="cdf11ac7-e8bc-4e03-b914-977da1892536" version="1.2.1" />
		<node id="5" name="Import XDF" position="(198.0, 663.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportxdf.OWImportXDF" title="Import XDF" uuid="4df1eb44-5edf-4e61-89f4-59f3a5a81360" version="1.2.1" />
		<node id="6" name="LSL Output" position="(512.0, 644.0)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output" uuid="b8704461-c503-436c-b08b-80da29ae4e6a" version="1.4.3" />
		<node id="7" name="Stream Data" position="(356.0, 647.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owstreamdata.OWStreamData" title="Stream Data" uuid="e9441918-f266-455e-8023-638efbd321a2" version="1.2.1" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="1" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="1" sink_channel="Data" sink_node_id="0" source_channel="Data" source_node_id="4" />
		<link enabled="true" id="2" sink_channel="Data" sink_node_id="3" source_channel="Data" source_node_id="2" />
		<link enabled="true" id="3" sink_channel="Data" sink_node_id="6" source_channel="Data" source_node_id="7" />
		<link enabled="true" id="4" sink_channel="Data" sink_node_id="7" source_channel="Data" source_node_id="5" />
	</links>
	<annotations>
		<text font-family="Helvetica" font-size="16" id="0" rect="(290.0, 356.0, 201.0, 54.0)">Gaze stream</text>
		<text font-family="Helvetica" font-size="16" id="1" rect="(281.0, 560.0, 238.0, 69.0)">EEG stream</text>
	</annotations>
	<thumbnail />
	<node_properties>
		<properties format="pickle" node_id="0">gAN9cQAoWAoAAABkYXRhX2R0eXBlcQFYBwAAAGZsb2F0NjRxAlgRAAAAaGl0Y2hfcHJvYmFiaWxp
dHlxA0cAAAAAAAAAAFgOAAAAaml0dGVyX3BlcmNlbnRxBEsFWAwAAABsb2dfcHJvZ3Jlc3NxBYlY
BwAAAGxvb3BpbmdxBohYCAAAAG1ldGFkYXRhcQd9cQhYCAAAAHJhbmRzZWVkcQlN54ZYEwAAAHNh
dmVkV2lkZ2V0R2VvbWV0cnlxCmNzaXAKX3VucGlja2xlX3R5cGUKcQtYDAAAAFB5UXQ1LlF0Q29y
ZXEMWAoAAABRQnl0ZUFycmF5cQ1DQgHZ0MsAAwAAAAADCwAAAVwAAAR0AAAClQAAAwwAAAF7AAAE
cwAAApQAAAAAAAAAAAeAAAADDAAAAXsAAARzAAAClHEOhXEPh3EQUnERWA4AAABzZXRfYnJlYWtw
b2ludHESiVgHAAAAc3BlZWR1cHETRz/wAAAAAAAAWAkAAABzdGFydF9wb3NxFEcAAAAAAAAAAFgQ
AAAAdGltZXN0YW1wX2ppdHRlcnEVRwAAAAAAAAAAWAYAAAB0aW1pbmdxFlgJAAAAd2FsbGNsb2Nr
cRdYDwAAAHVwZGF0ZV9pbnRlcnZhbHEYRz+keuFHrhR7dS4=
</properties>
		<properties format="pickle" node_id="1">gAN9cQAoWAkAAABjaHVua19sZW5xAUsAWBUAAABpZ25vcmVfc2lnbmFsX2NoYW5nZWRxAolYEwAA
AGtlZXBfc2luZ2xldG9uX2F4ZXNxA4lYDAAAAG1hcmtlcl9maWVsZHEEWAYAAABNYXJrZXJxBVgL
AAAAbWFya2VyX25hbWVxBlgRAAAAT3V0U3RyZWFtLW1hcmtlcnNxB1gQAAAAbWFya2VyX3NvdXJj
ZV9pZHEIWAAAAABxCVgMAAAAbWF4X2J1ZmZlcmVkcQpLPFgIAAAAbWV0YWRhdGFxC31xDFgXAAAA
bnVtZXJpY19sYWJlbF9wcmVjaXNpb25xDUsBWBgAAABudW1lcmljX21hcmtlcl9wcmVjaXNpb25x
DksDWBcAAAByZXNldF9pZl9sYWJlbHNfY2hhbmdlZHEPiVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRy
eXEQY3NpcApfdW5waWNrbGVfdHlwZQpxEVgMAAAAUHlRdDUuUXRDb3JlcRJYCgAAAFFCeXRlQXJy
YXlxE0NCAdnQywADAAAAAAMLAAABAgAABHQAAALvAAADDAAAASEAAARzAAAC7gAAAAAAAAAAB4AA
AAMMAAABIQAABHMAAALucRSFcRWHcRZScRdYDAAAAHNlbmRfbWFya2Vyc3EYiVgJAAAAc2VwYXJh
dG9ycRlYAQAAAC1xGlgOAAAAc2V0X2JyZWFrcG9pbnRxG4lYCQAAAHNvdXJjZV9pZHEcaAlYBQAA
AHNyYXRlcR1YDQAAACh1c2UgZGVmYXVsdClxHlgLAAAAc3RyZWFtX25hbWVxH1gKAAAARXllVHJh
Y2tlcnEgWAsAAABzdHJlYW1fdHlwZXEhWAgAAABQbGF5YmFja3EiWBMAAAB1c2VfZGF0YV90aW1l
c3RhbXBzcSOIWBYAAAB1c2VfbnVtcHlfb3B0aW1pemF0aW9ucSSJdS4=
</properties>
		<properties format="pickle" node_id="2">gAN9cQAoWA0AAABjaGFubmVsX25hbWVzcQFdcQJYCgAAAGRhdGFfZHR5cGVxA1gHAAAAZmxvYXQ2
NHEEWAsAAABkaWFnbm9zdGljc3EFiVgTAAAAZXhjbHVkZV9kZXNjX2ZpZWxkc3EGXXEHWAwAAABt
YXJrZXJfcXVlcnlxCFgAAAAAcQlYDAAAAG1heF9ibG9ja2xlbnEKTQAEWAoAAABtYXhfYnVmbGVu
cQtLHlgMAAAAbWF4X2NodW5rbGVucQxLAFgIAAAAbWV0YWRhdGFxDX1xDlgMAAAAbm9taW5hbF9y
YXRlcQ9YDQAAACh1c2UgZGVmYXVsdClxEFgJAAAAb21pdF9kZXNjcRGJWA8AAABwcmVhbGxvY19i
dWZmZXJxEohYDgAAAHByb2NfY2xvY2tzeW5jcROIWA0AAABwcm9jX2Rlaml0dGVycRSJWA8AAABw
cm9jX21vbm90b25pemVxFYlYDwAAAHByb2NfdGhyZWFkc2FmZXEWiVgFAAAAcXVlcnlxF1gVAAAA
bmFtZT0nUGxheWJhY2tTdHJlYW0ncRhYBwAAAHJlY292ZXJxGYhYFAAAAHJlc29sdmVfbWluaW11
bV90aW1lcRpHP+AAAAAAAABYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxG2NzaXAKX3VucGlja2xl
X3R5cGUKcRxYDAAAAFB5UXQ1LlF0Q29yZXEdWAoAAABRQnl0ZUFycmF5cR5DQgHZ0MsAAwAAAAAD
CwAAAVgAAAR0AAACmgAAAwwAAAF3AAAEcwAAApkAAAAAAAAAAAeAAAADDAAAAXcAAARzAAACmXEf
hXEgh3EhUnEiWA4AAABzZXRfYnJlYWtwb2ludHEjiXUu
</properties>
		<properties format="literal" node_id="3">{'metadata': {}, 'only_nonempty': True, 'print_channel': False, 'print_compact': True, 'print_data': False, 'print_markers': False, 'print_props': False, 'print_streams': [], 'print_time': False, 'print_trial': False, 'savedWidgetGeometry': None, 'set_breakpoint': False}</properties>
		<properties format="pickle" node_id="4">gAN9cQAoWA0AAABjbG91ZF9hY2NvdW50cQFYAAAAAHECWAwAAABjbG91ZF9idWNrZXRxA2gCWBEA
AABjbG91ZF9jcmVkZW50aWFsc3EEaAJYCgAAAGNsb3VkX2hvc3RxBVgHAAAARGVmYXVsdHEGWAgA
AABmaWxlbmFtZXEHWIEAAABDOi9Vc2Vycy94cmF5Mi9PbmVEcml2ZS9Eb2N1bWVudHMvTlROVS9E
YXRhSW5nMjAyMy9zMjAyMy9iYS9uZXVyb3B5cGUtcGlwZWxpbmUvaml0dGVyL2RhdGEvTFNMRGF0
YTIvTFNMRGF0YS9nYXplLWFuZC1ibGlua2luZy54ZGZxCFgTAAAAaGFuZGxlX2Nsb2NrX3Jlc2V0
c3EJiFgRAAAAaGFuZGxlX2Nsb2NrX3N5bmNxCohYFQAAAGhhbmRsZV9qaXR0ZXJfcmVtb3ZhbHEL
iFgOAAAAbWF4X21hcmtlcl9sZW5xDFgNAAAAKHVzZSBkZWZhdWx0KXENWAgAAABtZXRhZGF0YXEO
fXEPWBIAAAByZW9yZGVyX3RpbWVzdGFtcHNxEIlYDgAAAHJldGFpbl9zdHJlYW1zcRFoDVgTAAAA
c2F2ZWRXaWRnZXRHZW9tZXRyeXESY3NpcApfdW5waWNrbGVfdHlwZQpxE1gMAAAAUHlRdDUuUXRD
b3JlcRRYCgAAAFFCeXRlQXJyYXlxFUNCAdnQywADAAAAAAMMAAABnAAABHMAAAJzAAADDAAAAZwA
AARzAAACcwAAAAAAAAAAB4AAAAMMAAABnAAABHMAAAJzcRaFcReHcRhScRlYDgAAAHNldF9icmVh
a3BvaW50cRqJWAsAAAB1c2VfY2FjaGluZ3EbiVgPAAAAdXNlX3N0cmVhbW5hbWVzcRyJWAcAAAB2
ZXJib3NlcR2JdS4=
</properties>
		<properties format="pickle" node_id="5">gAN9cQAoWA0AAABjbG91ZF9hY2NvdW50cQFYAAAAAHECWAwAAABjbG91ZF9idWNrZXRxA2gCWBEA
AABjbG91ZF9jcmVkZW50aWFsc3EEaAJYCgAAAGNsb3VkX2hvc3RxBVgHAAAARGVmYXVsdHEGWAgA
AABmaWxlbmFtZXEHWHcAAABDOi9Vc2Vycy94cmF5Mi9PbmVEcml2ZS9Eb2N1bWVudHMvTlROVS9E
YXRhSW5nMjAyMy9zMjAyMy9iYS9uZXVyb3B5cGUtcGlwZWxpbmUvaml0dGVyL2RhdGEvTFNMRGF0
YTIvTFNMRGF0YS9yYXctZWVnLnhkZnEIWBMAAABoYW5kbGVfY2xvY2tfcmVzZXRzcQmIWBEAAABo
YW5kbGVfY2xvY2tfc3luY3EKiFgVAAAAaGFuZGxlX2ppdHRlcl9yZW1vdmFscQuIWA4AAABtYXhf
bWFya2VyX2xlbnEMWA0AAAAodXNlIGRlZmF1bHQpcQ1YCAAAAG1ldGFkYXRhcQ59cQ9YEgAAAHJl
b3JkZXJfdGltZXN0YW1wc3EQiVgOAAAAcmV0YWluX3N0cmVhbXNxEVgNAAAAKHVzZSBkZWZhdWx0
KXESWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cRNjc2lwCl91bnBpY2tsZV90eXBlCnEUWAwAAABQ
eVF0NS5RdENvcmVxFVgKAAAAUUJ5dGVBcnJheXEWQ0IB2dDLAAMAAAAAAwsAAAF9AAAEdAAAAnQA
AAMMAAABnAAABHMAAAJzAAAAAAAAAAAHgAAAAwwAAAGcAAAEcwAAAnNxF4VxGIdxGVJxGlgOAAAA
c2V0X2JyZWFrcG9pbnRxG4lYCwAAAHVzZV9jYWNoaW5ncRyJWA8AAAB1c2Vfc3RyZWFtbmFtZXNx
HYlYBwAAAHZlcmJvc2VxHol1Lg==
</properties>
		<properties format="pickle" node_id="6">gAN9cQAoWAkAAABjaHVua19sZW5xAUsAWBUAAABpZ25vcmVfc2lnbmFsX2NoYW5nZWRxAolYEwAA
AGtlZXBfc2luZ2xldG9uX2F4ZXNxA4lYDAAAAG1hcmtlcl9maWVsZHEEWAYAAABNYXJrZXJxBVgL
AAAAbWFya2VyX25hbWVxBlgRAAAAT3V0U3RyZWFtLW1hcmtlcnNxB1gQAAAAbWFya2VyX3NvdXJj
ZV9pZHEIWAAAAABxCVgMAAAAbWF4X2J1ZmZlcmVkcQpLPFgIAAAAbWV0YWRhdGFxC31xDFgXAAAA
bnVtZXJpY19sYWJlbF9wcmVjaXNpb25xDUsBWBgAAABudW1lcmljX21hcmtlcl9wcmVjaXNpb25x
DksDWBcAAAByZXNldF9pZl9sYWJlbHNfY2hhbmdlZHEPiVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRy
eXEQY3NpcApfdW5waWNrbGVfdHlwZQpxEVgMAAAAUHlRdDUuUXRDb3JlcRJYCgAAAFFCeXRlQXJy
YXlxE0NCAdnQywADAAAAAAMLAAABAgAABHQAAALvAAADDAAAASEAAARzAAAC7gAAAAAAAAAAB4AA
AAMMAAABIQAABHMAAALucRSFcRWHcRZScRdYDAAAAHNlbmRfbWFya2Vyc3EYiVgJAAAAc2VwYXJh
dG9ycRlYAQAAAC1xGlgOAAAAc2V0X2JyZWFrcG9pbnRxG4lYCQAAAHNvdXJjZV9pZHEcaAlYBQAA
AHNyYXRlcR1YDQAAACh1c2UgZGVmYXVsdClxHlgLAAAAc3RyZWFtX25hbWVxH1gVAAAATGl2ZUFt
cFNOLTA1NjMwOS0wNTUzcSBYCwAAAHN0cmVhbV90eXBlcSFYCAAAAFBsYXliYWNrcSJYEwAAAHVz
ZV9kYXRhX3RpbWVzdGFtcHNxI4hYFgAAAHVzZV9udW1weV9vcHRpbWl6YXRpb25xJIl1Lg==
</properties>
		<properties format="literal" node_id="7">{'data_dtype': 'float64', 'hitch_probability': 0.0, 'jitter_percent': 5, 'log_progress': False, 'looping': True, 'metadata': {}, 'randseed': 34535, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'speedup': 1.0, 'start_pos': 0.0, 'timestamp_jitter': 0.0, 'timing': 'wallclock', 'update_interval': 0.04}</properties>
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
            "node5",
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
            "node8",
            "data",
            "node7",
            "data"
        ],
        [
            "node6",
            "data",
            "node8",
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
            "uuid": "1ad00b73-42f0-42d4-bcd5-54c406f77c59"
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
                    "value": "EyeTracker"
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
            "uuid": "4bdd3433-d698-4002-ac13-d836b5ea0181"
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
            "uuid": "7701e74e-8d91-4933-bf32-899d1a2c429d"
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
            "uuid": "1a302bcf-a868-41d3-a1cf-7e0578fdf802"
        },
        "node5": {
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
                    "value": "C:/Users/xray2/OneDrive/Documents/NTNU/DataIng2023/s2023/ba/neuropype-pipeline/jitter/data/LSLData2/LSLData/gaze-and-blinking.xdf"
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
            "uuid": "cdf11ac7-e8bc-4e03-b914-977da1892536"
        },
        "node6": {
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
                    "value": "C:/Users/xray2/OneDrive/Documents/NTNU/DataIng2023/s2023/ba/neuropype-pipeline/jitter/data/LSLData2/LSLData/raw-eeg.xdf"
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
            "uuid": "4df1eb44-5edf-4e61-89f4-59f3a5a81360"
        },
        "node7": {
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
                    "value": "LiveAmpSN-056309-0553"
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
            "uuid": "b8704461-c503-436c-b08b-80da29ae4e6a"
        },
        "node8": {
            "class": "StreamData",
            "module": "neuropype.nodes.formatting.StreamData",
            "params": {
                "data_dtype": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "float64"
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
            "uuid": "e9441918-f266-455e-8023-638efbd321a2"
        }
    },
    "version": 1.1
}</patch>
</scheme>
