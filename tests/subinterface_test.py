import config.main as config
from click.testing import CliRunner
from utilities_common.db import Db

# CLI command:
# sudo config subinterface add Ethernet104.4092

class TestSubinterface(object):
    def test_subinterface_add(self):
        """ Verify subinterface name length = 15 characters """
        runner = CliRunner()
        db = Db()
        obj = {'db': db.cfgdb}

        ports = db.cfgdb.get_table('PORT')
        port = list(ports.keys())[0]
        print(port)

        result = runner.invoke(config.config.commands["subinterface"].commands["add"], ["Ethernet100.100"], obj=obj)
        print(result.exit_code, result.output)
        assert result.exit_code == 0
        assert "Ethernet100.100" in db.cfgdb.get_table('VLAN_SUB_INTERFACE')

    def test_subinterface_add_invalid_name(self):
        """ Invalid subinterface name length > 15 characters """
        runner = CliRunner()
        db = Db()
        obj = {'db': db.cfgdb}

        result = runner.invoke(config.config.commands["subinterface"].commands["add"], ["Ethernet104.4092"], obj=obj)
        print(result.exit_code, result.output)
        assert result.exit_code != 0
        assert "Ethernet104.4092" not in db.cfgdb.get_table('VLAN_SUB_INTERFACE')
