import config.main as config
from click.testing import CliRunner
from utilities_common.db import Db

class TestSubinterface(object):
    def test_subinterface_add(self):
        runner = CliRunner()
        db = Db()
        obj = {'db': db.cfgdb}

        ports = db.cfgdb.get_table('PORT')
        port = list(ports.keys())[0]
        # sudo config subinterface add Ethernet124.4092
        # result = runner.invoke(config.config.commands["sub"].commands["run"], ["param1", "param2"], obj=obj)
        result = runner.invoke(config.config.commands["subinterface"].commands["add"], ["Ethernet0.100"], obj=obj)
        print(result.exit_code, result.output)
        assert result.exit_code == 0
        assert "Ethernet0.100" in db.cfgdb.get_table('VLAN_SUB_INTERFACE')
        # assert 'expected_output' in result.output

    def test_subinterface_add_invalid_name(self):
        """ Invalid subinterface name length > 15 characters """
        runner = CliRunner()
        db = Db()
        obj = {'db': db.cfgdb}

        result = runner.invoke(config.config.commands["subinterface"].commands["add"], ["Ethernet104.4094"], obj=obj)
        print(result.exit_code, result.output)
        assert result.exit_code != 0
        assert "Ethernet104.4094" not in db.cfgdb.get_table('VLAN_SUB_INTERFACE')
